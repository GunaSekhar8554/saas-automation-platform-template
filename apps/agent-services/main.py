"""
AI Agent Services - Main Entry Point
Orchestrates various AI agents for SAP integration and automation
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
import logging

from shared.config import AgentConfig
from shared.monitoring import setup_monitoring
from llm_agents.orchestrator import AgentOrchestrator
from migration_agents.service import MigrationAgentService
from connectors.sap_connector import SAPConnectorService

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config = AgentConfig()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    # Startup
    logger.info("Starting Agent Services...")
    await setup_monitoring()
    
    # Initialize services
    app.state.orchestrator = AgentOrchestrator()
    app.state.migration_service = MigrationAgentService()
    app.state.sap_connector = SAPConnectorService()
    
    yield
    
    # Shutdown
    logger.info("Shutting down Agent Services...")

app = FastAPI(
    title="AI Agent Services",
    description="Microservice for AI-powered SAP integration and automation agents",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "agent-services",
        "version": "1.0.0"
    }

@app.get("/agents/status")
async def get_agents_status():
    """Get status of all agents"""
    try:
        orchestrator = app.state.orchestrator
        return await orchestrator.get_all_agents_status()
    except Exception as e:
        logger.error(f"Failed to get agents status: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve agents status")

@app.post("/agents/migration/start")
async def start_migration_task(migration_request: dict):
    """Start a migration task"""
    try:
        migration_service = app.state.migration_service
        task_id = await migration_service.start_migration(migration_request)
        return {"task_id": task_id, "status": "started"}
    except Exception as e:
        logger.error(f"Failed to start migration: {e}")
        raise HTTPException(status_code=500, detail="Failed to start migration task")

@app.get("/agents/migration/{task_id}/status")
async def get_migration_status(task_id: str):
    """Get migration task status"""
    try:
        migration_service = app.state.migration_service
        status = await migration_service.get_task_status(task_id)
        return status
    except Exception as e:
        logger.error(f"Failed to get migration status: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve migration status")

@app.post("/connectors/sap/test")
async def test_sap_connection(connection_config: dict):
    """Test SAP connection"""
    try:
        sap_connector = app.state.sap_connector
        result = await sap_connector.test_connection(connection_config)
        return result
    except Exception as e:
        logger.error(f"SAP connection test failed: {e}")
        raise HTTPException(status_code=500, detail="SAP connection test failed")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
        log_level="info"
    )
