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
    assert b"Welcome to the Request Dispatch Service!" in res.data

def test_health_check(client):
    """Test the health check endpoint."""
    res = client.get('/health')
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}

# NEW TEST for the /fetch endpoint
def test_fetch_success(client):
    """Test the /fetch endpoint with a valid URL."""
    # We use a mock server URL for a reliable test
    res = client.post('/fetch', json={'url': 'http://httpbin.org/html'})
    assert res.status_code == 200
    assert b'<h1>Herman Melville - Moby-Dick</h1>' in res.data

# NEW TEST for the /fetch endpoint's error handling
def test_fetch_missing_url(client):
    """Test the /fetch endpoint with a missing URL in the payload."""
    res = client.post('/fetch', json={'wrong_key': 'some_value'})
    assert res.status_code == 400
    assert res.get_json() == {"error": "URL is required"}