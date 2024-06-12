from fastapi.testclient import TestClient
from app.main import app
from app.database import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.database import get_db

import pytest

from app.oauth2 import create_acess_token
from app import models

#from alembic import command

SQLALCHEMY_DATABASE_URL = f"""postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}_test"""

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture()
def session():
    # command.upgrade("head")
    # command.downgrade("base")
    Base.metadata.drop_all(bind=engine) # drop the tables before the test
    Base.metadata.create_all(bind=engine) # create the tables before the test
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

@pytest.fixture()
def test_user(client):
    user_data = {"email": "rian@gmail.com", "password": "rian"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 201

    new_user = response.json()
    new_user['password'] = user_data['password']
    return new_user

@pytest.fixture
def token(test_user):
    return create_acess_token({"user_id": test_user['id']})

@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    return client

@pytest.fixture
def test_posts(test_user, session):
    posts_data = [{
        "title": "bitcoin in bull market",
        "content": "its increasing its value",
        "owner_id": test_user['id']
    }, {
        "title": "corn harvest",
        "content": "increasing this year",
        "owner_id": test_user['id']
    }, {
        "title": "gas",
        "content": "very expensive",
        "owner_id": test_user['id']
    }]

    def create_post_model(post):
        return models.Post(**post)
    
    post_map = map(create_post_model, posts_data)
    posts = list(post_map)

    session.add_all(posts)
    session.commit()
    posts = session.query(models.Post).all()
    return posts