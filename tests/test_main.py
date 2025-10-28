import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'OK'
    assert 'message' in data

def test_root_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Student Feedback Form' in response.data
