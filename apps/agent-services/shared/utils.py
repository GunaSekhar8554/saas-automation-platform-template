"""
Shared utilities for agent services
"""
import uuid
import json
import logging
from datetime import datetime
from typing import Any, Dict, Optional
from dataclasses import dataclass, asdict


@dataclass
class TaskResult:
    """Standard task result structure"""
    task_id: str
    status: str
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    created_at: datetime = None
    completed_at: Optional[datetime] = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.utcnow()
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def generate_task_id() -> str:
    """Generate a unique task ID"""
    return str(uuid.uuid4())


def setup_logger(name: str, level: str = "INFO") -> logging.Logger:
    """Setup logger with consistent formatting"""
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger


def safe_json_loads(data: str, default: Any = None) -> Any:
    """Safely parse JSON with fallback"""
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        return default


def validate_connection_config(config: Dict[str, Any], required_fields: list) -> bool:
    """Validate connection configuration"""
    return all(field in config and config[field] for field in required_fields)
