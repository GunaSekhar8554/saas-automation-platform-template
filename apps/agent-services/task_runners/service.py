"""
Task Runner Service - Manages and executes background tasks
"""
import asyncio
from typing import Dict, Any, List, Optional, Callable
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import logging

from ..shared.utils import generate_task_id, setup_logger
from ..shared.monitoring import monitor_performance, metrics

logger = setup_logger(__name__)


class TaskStatus(Enum):
    """Task execution status"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    RETRYING = "retrying"


class TaskPriority(Enum):
    """Task priority levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


@dataclass
class Task:
    """Represents a background task"""
    task_id: str
    name: str
    function: Callable
    args: tuple = field(default_factory=tuple)
    kwargs: dict = field(default_factory=dict)
    priority: TaskPriority = TaskPriority.MEDIUM
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    result: Optional[Any] = None
    error: Optional[str] = None
    retries: int = 0
    max_retries: int = 3
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "name": self.name,
            "priority": self.priority.value,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "result": self.result,
            "error": self.error,
            "retries": self.retries,
            "max_retries": self.max_retries
        }


class TaskQueue:
    """Priority-based task queue"""
    
    def __init__(self):
        self.queues = {
            TaskPriority.URGENT: asyncio.Queue(),
            TaskPriority.HIGH: asyncio.Queue(),
            TaskPriority.MEDIUM: asyncio.Queue(),
            TaskPriority.LOW: asyncio.Queue()
        }
    
    async def put(self, task: Task):
        """Add task to appropriate priority queue"""
        await self.queues[task.priority].put(task)
        metrics.increment_counter(f"tasks_queued_{task.priority.value}")
    
    async def get(self) -> Task:
        """Get next task based on priority"""
        # Check queues in priority order
        for priority in [TaskPriority.URGENT, TaskPriority.HIGH, TaskPriority.MEDIUM, TaskPriority.LOW]:
            queue = self.queues[priority]
            if not queue.empty():
                task = await queue.get()
                metrics.increment_counter(f"tasks_dequeued_{priority.value}")
                return task
        
        # If all queues are empty, wait for any task
        while True:
            for priority in [TaskPriority.URGENT, TaskPriority.HIGH, TaskPriority.MEDIUM, TaskPriority.LOW]:
                queue = self.queues[priority]
                try:
                    task = queue.get_nowait()
                    metrics.increment_counter(f"tasks_dequeued_{priority.value}")
                    return task
                except asyncio.QueueEmpty:
                    continue
            await asyncio.sleep(0.1)  # Small delay to prevent busy waiting


class TaskRunner:
    """Manages and executes background tasks"""
    
    def __init__(self, max_workers: int = 5):
        self.max_workers = max_workers
        self.task_queue = TaskQueue()
        self.active_tasks: Dict[str, Task] = {}
        self.completed_tasks: Dict[str, Task] = {}
        self.workers: List[asyncio.Task] = []
        self.is_running = False
    
    async def start(self):
        """Start the task runner"""
        if self.is_running:
            return
        
        self.is_running = True
        
        # Start worker coroutines
        for i in range(self.max_workers):
            worker = asyncio.create_task(self._worker(f"worker-{i}"))
            self.workers.append(worker)
        
        logger.info(f"Started task runner with {self.max_workers} workers")
    
    async def stop(self):
        """Stop the task runner"""
        if not self.is_running:
            return
        
        self.is_running = False
        
        # Cancel all workers
        for worker in self.workers:
            worker.cancel()
        
        # Wait for workers to finish
        await asyncio.gather(*self.workers, return_exceptions=True)
        
        self.workers.clear()
        logger.info("Stopped task runner")
    
    async def _worker(self, worker_name: str):
        """Worker coroutine that processes tasks"""
        logger.info(f"Worker {worker_name} started")
        
        while self.is_running:
            try:
                # Get next task from queue
                task = await self.task_queue.get()
                
                # Move task to active tasks
                self.active_tasks[task.task_id] = task
                
                # Execute the task
                await self._execute_task(task, worker_name)
                
                # Move task to completed tasks
                if task.task_id in self.active_tasks:
                    del self.active_tasks[task.task_id]
                self.completed_tasks[task.task_id] = task
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Worker {worker_name} error: {e}")
        
        logger.info(f"Worker {worker_name} stopped")
    
    @monitor_performance("execute_task")
    async def _execute_task(self, task: Task, worker_name: str):
        """Execute a single task"""
        task.status = TaskStatus.RUNNING
        task.started_at = datetime.utcnow()
        
        logger.info(f"Worker {worker_name} executing task {task.task_id}: {task.name}")
        
        try:
            # Execute the task function
            if asyncio.iscoroutinefunction(task.function):
                result = await task.function(*task.args, **task.kwargs)
            else:
                result = task.function(*task.args, **task.kwargs)
            
            task.result = result
            task.status = TaskStatus.COMPLETED
            task.completed_at = datetime.utcnow()
            
            metrics.increment_counter("tasks_completed")
            logger.info(f"Task {task.task_id} completed successfully")
            
        except Exception as e:
            task.error = str(e)
            task.retries += 1
            
            if task.retries <= task.max_retries:
                task.status = TaskStatus.RETRYING
                logger.warning(f"Task {task.task_id} failed, retrying ({task.retries}/{task.max_retries}): {e}")
                
                # Re-queue the task for retry
                await self.task_queue.put(task)
                return
            else:
                task.status = TaskStatus.FAILED
                task.completed_at = datetime.utcnow()
                
                metrics.increment_counter("tasks_failed")
                logger.error(f"Task {task.task_id} failed permanently after {task.retries} retries: {e}")
    
    async def submit_task(
        self,
        name: str,
        function: Callable,
        args: tuple = (),
        kwargs: dict = None,
        priority: TaskPriority = TaskPriority.MEDIUM,
        max_retries: int = 3
    ) -> str:
        """Submit a new task for execution"""
        task_id = generate_task_id()
        
        task = Task(
            task_id=task_id,
            name=name,
            function=function,
            args=args,
            kwargs=kwargs or {},
            priority=priority,
            max_retries=max_retries
        )
        
        await self.task_queue.put(task)
        
        logger.info(f"Submitted task {task_id}: {name} with priority {priority.value}")
        metrics.increment_counter("tasks_submitted")
        
        return task_id
    
    def get_task_status(self, task_id: str) -> Optional[Dict[str, Any]]:
        """Get status of a specific task"""
        # Check active tasks first
        if task_id in self.active_tasks:
            return self.active_tasks[task_id].to_dict()
        
        # Check completed tasks
        if task_id in self.completed_tasks:
            return self.completed_tasks[task_id].to_dict()
        
        return None
    
    def get_active_tasks(self) -> List[Dict[str, Any]]:
        """Get all active tasks"""
        return [task.to_dict() for task in self.active_tasks.values()]
    
    def get_completed_tasks(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Get completed tasks (most recent first)"""
        tasks = list(self.completed_tasks.values())
        tasks.sort(key=lambda t: t.completed_at or t.created_at, reverse=True)
        return [task.to_dict() for task in tasks[:limit]]
    
    def get_queue_status(self) -> Dict[str, Any]:
        """Get status of task queues"""
        return {
            "urgent": self.task_queue.queues[TaskPriority.URGENT].qsize(),
            "high": self.task_queue.queues[TaskPriority.HIGH].qsize(),
            "medium": self.task_queue.queues[TaskPriority.MEDIUM].qsize(),
            "low": self.task_queue.queues[TaskPriority.LOW].qsize(),
            "active_tasks": len(self.active_tasks),
            "completed_tasks": len(self.completed_tasks),
            "workers": len(self.workers),
            "is_running": self.is_running
        }
    
    async def cancel_task(self, task_id: str) -> bool:
        """Cancel a task"""
        if task_id in self.active_tasks:
            task = self.active_tasks[task_id]
            task.status = TaskStatus.CANCELLED
            task.completed_at = datetime.utcnow()
            
            logger.info(f"Cancelled task {task_id}")
            metrics.increment_counter("tasks_cancelled")
            
            return True
        
        return False


# Example task functions for testing
async def example_async_task(duration: int, message: str = "Task completed") -> Dict[str, Any]:
    """Example async task that takes some time"""
    await asyncio.sleep(duration)
    return {"message": message, "duration": duration}


def example_sync_task(x: int, y: int) -> int:
    """Example synchronous task"""
    return x + y


# Global task runner instance
task_runner = TaskRunner()
