import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_square_success(client):
    response = client.post('/square', json={"number": 4})
    assert response.status_code == 200
    assert response.get_json()['square'] == 16

def test_square_failure(client):
    response = client.post('/square', json={"num": 4})
    assert response.status_code == 400
