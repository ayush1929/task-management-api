import pytest
import sys
import os

# Ensure the app.py file's path is in the system's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_task(client):
    response = client.post('/tasks', json={
        'title': 'Test Task',
        'description': 'This is a test task.'
    })
    assert response.status_code == 201
    assert response.json['title'] == 'Test Task'

def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_update_task(client):
    client.post('/tasks', json={
        'title': 'Test Task',
        'description': 'This is a test task.'
    })
    response = client.put('/tasks/1', json={
        'title': 'Updated Task',
        'description': 'Updated description.'
    })
    assert response.status_code == 200
    assert response.json['title'] == 'Updated Task'

def test_delete_task(client):
    client.post('/tasks', json={
        'title': 'Test Task',
        'description': 'This is a test task.'
    })
    response = client.delete('/tasks/1')
    assert response.status_code == 200
    assert response.json['message'] == 'Task deleted'
