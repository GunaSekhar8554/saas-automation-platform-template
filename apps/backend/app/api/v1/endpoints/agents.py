from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_agents():
    """List agents endpoint."""
    return {"message": "List agents endpoint - to be implemented"}


@router.get("/{agent_id}")
async def get_agent(agent_id: str):
    """Get agent by ID endpoint."""
    return {"message": f"Get agent {agent_id} endpoint - to be implemented"}


@router.post("/")
async def create_agent():
    """Create agent endpoint."""
    return {"message": "Create agent endpoint - to be implemented"}


@router.post("/{agent_id}/execute")
async def execute_agent(agent_id: str):
    """Execute agent endpoint."""
    return {"message": f"Execute agent {agent_id} endpoint - to be implemented"}
