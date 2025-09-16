from fastapi import APIRouter
from app.api.v1.endpoints import auth, users, tenants, migrations, agents, health

api_router = APIRouter()

# Health check
api_router.include_router(health.router, prefix="/health", tags=["health"])

# Authentication
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])

# Core entities
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(tenants.router, prefix="/tenants", tags=["tenants"])
api_router.include_router(migrations.router, prefix="/migrations", tags=["migrations"])
api_router.include_router(agents.router, prefix="/agents", tags=["agents"])
