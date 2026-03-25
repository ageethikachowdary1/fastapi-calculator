from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "Calculator" in response.text


def test_add_endpoint():
    response = client.post("/calculate", data={"a": 2, "b": 3, "operation": "add"})
    assert response.status_code == 200
    assert "Result: 5.0" in response.text or "Result: 5" in response.text


def test_subtract_endpoint():
    response = client.post("/calculate", data={"a": 10, "b": 4, "operation": "subtract"})
    assert response.status_code == 200
    assert "Result: 6.0" in response.text or "Result: 6" in response.text


def test_multiply_endpoint():
    response = client.post("/calculate", data={"a": 6, "b": 7, "operation": "multiply"})
    assert response.status_code == 200
    assert "Result: 42.0" in response.text or "Result: 42" in response.text


def test_divide_endpoint():
    response = client.post("/calculate", data={"a": 8, "b": 2, "operation": "divide"})
    assert response.status_code == 200
    assert "Result: 4.0" in response.text or "Result: 4" in response.text


def test_divide_by_zero_endpoint():
    response = client.post("/calculate", data={"a": 5, "b": 0, "operation": "divide"})
    assert response.status_code == 200
    assert "Cannot divide by zero" in response.text


def test_invalid_operation():
    response = client.post("/calculate", data={"a": 5, "b": 2, "operation": "power"})
    assert response.status_code == 200
    assert "Invalid operation" in response.text
