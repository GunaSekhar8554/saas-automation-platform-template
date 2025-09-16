from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.core.config import settings
import asyncio

router = APIRouter()


@router.get("/")
async def health_check():
    """Basic health check endpoint."""
    return {
        "status": "healthy",
        "service": "backend",
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT
    }


@router.get("/detailed")
async def detailed_health_check(db: AsyncSession = Depends(get_session)):
    """Detailed health check including database connectivity."""
    health_status = {
        "status": "healthy",
        "service": "backend",
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "checks": {}
    }
    
    # Database check
    try:
        await db.execute("SELECT 1")
        health_status["checks"]["database"] = "healthy"
    except Exception as e:
        health_status["checks"]["database"] = f"unhealthy: {str(e)}"
        health_status["status"] = "unhealthy"
    
    # Redis check (placeholder)
    health_status["checks"]["redis"] = "not_implemented"
    
    return health_status


@router.get("/ready")
async def readiness_check():
    """Kubernetes readiness probe."""
    return {"status": "ready"}


@router.get("/live")
async def liveness_check():
    """Kubernetes liveness probe."""
    return {"status": "alive"}
