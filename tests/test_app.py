import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(client):
    """Test the home page."""
    res = client.get('/')
    assert res.status_code == 200
    # assert b"Request-Dispatch-Service is running!" in res.data
    assert b"Welcome to the Request Dispatch Service!" in res.data

def test_health_check(client):
    """Test the health check endpoint."""
    res = client.get('/health')
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}