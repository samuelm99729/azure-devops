import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_submit_feedback(client):
    data = {
        'name': 'Test User',
        'subject': 'Test Subject',
        'rating': '5',
        'comments': 'Great app!'
    }
    response = client.post('/submit', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b'Feedbacks' in response.data  # Assuming feedbacks page has this

def test_view_feedbacks(client):
    response = client.get('/feedbacks')
    assert response.status_code == 200
    assert b'Feedbacks' in response.data  # Assuming the template has this text
