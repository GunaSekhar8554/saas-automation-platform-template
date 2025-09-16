from pydantic_settings import BaseSettings
from typing import List, Optional
import secrets


class Settings(BaseSettings):
    # Project Info
    PROJECT_NAME: str = "SaaS Automation Platform"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "AI-powered PI/PO to SAP BTP migration platform"
    
    # API
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    ALGORITHM: str = "HS256"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:3002",
        "http://localhost:3003",
        "http://localhost:3004",
        "https://localhost:3000",
        "https://localhost:3001",
        "https://localhost:3002",
        "https://localhost:3003",
        "https://localhost:3004",
    ]
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1", "*"]
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/saas_platform"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # Environment
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    # External APIs
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    
    # SAP Endpoints
    SAP_PI_ENDPOINT: Optional[str] = None
    SAP_PO_ENDPOINT: Optional[str] = None
    SAP_BTP_ENDPOINT: Optional[str] = None
    
    # Monitoring
    SENTRY_DSN: Optional[str] = None
    LOG_LEVEL: str = "INFO"
    
    # Agent Configuration
    AGENT_CONCURRENCY_LIMIT: int = 10
    TASK_TIMEOUT: int = 300
    MAX_RETRIES: int = 3
    
    # Multi-tenancy
    DEFAULT_TENANT_ID: str = "default"
    TENANT_ISOLATION_MODE: str = "schema"  # "schema" or "row"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
