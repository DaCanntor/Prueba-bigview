from fastapi.testclient import TestClient
from main import app

user = TestClient(app)

def setup_function():
    global users
    users = {"1": {"name": "Alice", "age": 30}, "2": {"name": "Bob", "age": 25}}

def test_get_existe_usuario():
    response = user.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Alice", "age": 30}

def test_get_noexiste_usuario():
    response = user.get("/users/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_crear_nuevo_usuario():
    response = user.post("/users/", params={"user_id": "3", "name": "Charlie", "age": 28})
    assert response.status_code == 200
    assert response.json() == {"name": "Charlie", "age": 28}

def test_crear_usuario_existente():
    response = user.post("/users/", params={"user_id": "1", "name": "NewName", "age": 40})
    assert response.status_code == 400
    assert response.json() == {"detail": "User already exists"}

def test_crear_usuario_edad_invalida_type():
    response = user.post("/users/", params={"user_id": "5", "name": "Test", "age": "abc"})
    assert response.status_code == 422

def test_crear_usuario_incompleto():
    response = user.post("/users/", params={"user_id": "6"})
    assert response.status_code == 422