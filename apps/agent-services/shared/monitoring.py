"""
Monitoring and observability setup for agent services
"""
import logging
import time
from typing import Dict, Any
from functools import wraps

logger = logging.getLogger(__name__)


async def setup_monitoring():
    """Initialize monitoring and observability"""
    logger.info("Setting up monitoring...")
    # Add your monitoring setup here (Prometheus, etc.)
    

def monitor_performance(func_name: str):
    """Decorator to monitor function performance"""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = await func(*args, **kwargs)
                duration = time.time() - start_time
                logger.info(f"{func_name} completed in {duration:.2f}s")
                return result
            except Exception as e:
                duration = time.time() - start_time
                logger.error(f"{func_name} failed after {duration:.2f}s: {e}")
                raise
        return wrapper
    return decorator


class MetricsCollector:
    """Collect and store metrics"""
    
    def __init__(self):
        self.metrics: Dict[str, Any] = {}
    
    def increment_counter(self, name: str, value: int = 1):
        """Increment a counter metric"""
        if name not in self.metrics:
            self.metrics[name] = 0
        self.metrics[name] += value
    
    def set_gauge(self, name: str, value: float):
        """Set a gauge metric"""
        self.metrics[name] = value
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get all metrics"""
        return self.metrics.copy()


# Global metrics collector
metrics = MetricsCollector()
