import requests

BASE_URL = "http://localhost:5000"

def test_home():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert "Hello, DevOps Exam" in response.text

def test_db_connection():
    response = requests.get(f"{BASE_URL}/db-test")
    assert response.status_code == 200
    assert "Database Connected Successfully" in response.text
