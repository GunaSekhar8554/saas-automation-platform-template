from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_users():
    """List users endpoint."""
    return {"message": "List users endpoint - to be implemented"}


@router.get("/{user_id}")
async def get_user(user_id: str):
    """Get user by ID endpoint."""
    return {"message": f"Get user {user_id} endpoint - to be implemented"}


@router.post("/")
async def create_user():
    """Create user endpoint."""
    return {"message": "Create user endpoint - to be implemented"}
