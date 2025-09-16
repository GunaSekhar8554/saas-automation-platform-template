import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "SaaS Automation Platform API"
    assert "version" in data


def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_api_health_endpoint():
    """Test the API health endpoint."""
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "backend"


@pytest.mark.asyncio
async def test_detailed_health_check():
    """Test the detailed health check endpoint."""
    response = client.get("/api/v1/health/detailed")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "checks" in data


def test_readiness_probe():
    """Test the Kubernetes readiness probe."""
    response = client.get("/api/v1/health/ready")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ready"


def test_liveness_probe():
    """Test the Kubernetes liveness probe."""
    response = client.get("/api/v1/health/live")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "alive"
