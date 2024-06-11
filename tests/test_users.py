from app import schemas
from .database import client, session

def test_root(client):
    response = client.get("/")
    print(response.json().get('message'))
    assert response.json().get('message') == 'Hello World'
    assert response.status_code == 200

def test_create_user(client):
    response = client.post("/users/", json={"email": "rian@gmail.com", "password": "rian"})
    new_user = schemas.UserResponse(**response.json())
    assert new_user.email == "rian@gmail.com"
    assert response.status_code == 201