"""
Tests for agent services
"""
import pytest
import asyncio
from httpx import AsyncClient

from ..main import app


@pytest.fixture
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def client():
    """Create test client"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    """Test health check endpoint"""
    response = await client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "agent-services"


@pytest.mark.asyncio
async def test_agents_status(client: AsyncClient):
    """Test agents status endpoint"""
    response = await client.get("/agents/status")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
async def test_sap_connection_test(client: AsyncClient):
    """Test SAP connection test endpoint"""
    connection_config = {
        "type": "sap_pi",
        "host": "test-host",
        "port": 8000,
        "username": "testuser"
    }
    
    response = await client.post("/connectors/sap/test", json=connection_config)
    assert response.status_code == 200
    data = response.json()
    assert "success" in data
