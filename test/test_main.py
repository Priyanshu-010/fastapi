from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

# Test Home API

def test_home():
  response = client.get("/")
  #Status Code check
  assert response.status_code == 200
  # Response Data check
  assert response.json() == {"message": "Hello, World!"}

def test_add():
  response = client.get("add?a=2&b=2")
  assert response.status_code == 200
  assert response.json() == {"result": 4}