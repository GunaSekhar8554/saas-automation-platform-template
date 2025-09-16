from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_tenants():
    """List tenants endpoint."""
    return {"message": "List tenants endpoint - to be implemented"}


@router.get("/{tenant_id}")
async def get_tenant(tenant_id: str):
    """Get tenant by ID endpoint."""
    return {"message": f"Get tenant {tenant_id} endpoint - to be implemented"}


@router.post("/")
async def create_tenant():
    """Create tenant endpoint."""
    return {"message": "Create tenant endpoint - to be implemented"}
