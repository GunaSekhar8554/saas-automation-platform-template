from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
import time
import uuid
from app.core.config import settings


def setup_middleware(app: FastAPI):
    """Set up all middleware for the FastAPI application."""
    
    # Request ID middleware
    @app.middleware("http")
    async def add_request_id(request: Request, call_next):
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response
    
    # Timing middleware
    @app.middleware("http")
    async def add_process_time(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response
    
    # Tenant middleware (placeholder)
    @app.middleware("http")
    async def tenant_middleware(request: Request, call_next):
        # Extract tenant from header, subdomain, or JWT token
        tenant_id = request.headers.get("X-Tenant-ID", settings.DEFAULT_TENANT_ID)
        request.state.tenant_id = tenant_id
        response = await call_next(request)
        return response
    
    # Global exception handler
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={
                "detail": "Internal server error",
                "request_id": getattr(request.state, "request_id", None)
            }
        )
