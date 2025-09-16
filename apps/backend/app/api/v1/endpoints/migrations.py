from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_migrations():
    """List migrations endpoint."""
    return {"message": "List migrations endpoint - to be implemented"}


@router.get("/{migration_id}")
async def get_migration(migration_id: str):
    """Get migration by ID endpoint."""
    return {"message": f"Get migration {migration_id} endpoint - to be implemented"}


@router.post("/")
async def create_migration():
    """Create migration endpoint."""
    return {"message": "Create migration endpoint - to be implemented"}


@router.post("/{migration_id}/start")
async def start_migration(migration_id: str):
    """Start migration endpoint."""
    return {"message": f"Start migration {migration_id} endpoint - to be implemented"}
