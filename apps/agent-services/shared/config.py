"""
Shared configuration for agent services
"""
import os
from typing import List
from pydantic import BaseSettings


class AgentConfig(BaseSettings):
    """Configuration settings for agent services"""
    
    # Service settings
    service_name: str = "agent-services"
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    
    # Database settings
    database_url: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/saas_platform")
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    
    # AI Provider settings
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    
    # SAP Connection settings
    sap_pi_host: str = os.getenv("SAP_PI_HOST", "")
    sap_po_host: str = os.getenv("SAP_PO_HOST", "")
    sap_btp_url: str = os.getenv("SAP_BTP_URL", "")
    
    # Security settings
    secret_key: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    allowed_origins: List[str] = ["http://localhost:3000", "http://localhost:3004"]
    
    # Agent settings
    max_concurrent_agents: int = int(os.getenv("MAX_CONCURRENT_AGENTS", "10"))
    agent_timeout: int = int(os.getenv("AGENT_TIMEOUT", "300"))  # 5 minutes
    
    # Monitoring settings
    enable_monitoring: bool = os.getenv("ENABLE_MONITORING", "true").lower() == "true"
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    
    class Config:
        env_file = ".env"
