from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
async def login():
    """User login endpoint."""
    return {"message": "Login endpoint - to be implemented"}


@router.post("/logout")
async def logout():
    """User logout endpoint."""
    return {"message": "Logout endpoint - to be implemented"}


@router.post("/refresh")
async def refresh_token():
    """Refresh JWT token endpoint."""
    return {"message": "Refresh token endpoint - to be implemented"}
