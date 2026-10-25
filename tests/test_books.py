"""API tests use a separate temporary SQLite database."""
import os
import tempfile

# Set the database URL before importing the application modules.
TEST_DB = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
TEST_DB.close()
os.environ["TEST_DATABASE_URL"] = TEST_DB.name

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.database import Base, get_db
from app.main import app

# Override the app's DB dependency with an isolated in-memory test database.
test_engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
Base.metadata.create_all(bind=test_engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def sample_book():
    return {
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "isbn": "9780135957059",
        "publication_year": 2019,
        "category": "Programming",
        "available": True,
    }


def test_home_and_health():
    assert client.get("/").status_code == 200
    assert client.get("/health").json()["status"] == "ok"


def test_create_list_read_update_delete_book():
    created = client.post("/books/", json=sample_book())
    assert created.status_code == 201
    book_id = created.json()["book_id"]

    assert client.get("/books/").json()[0]["title"] == "The Pragmatic Programmer"
    assert client.get(f"/books/{book_id}").status_code == 200

    updated_data = sample_book()
    updated_data["title"] = "The Pragmatic Programmer - Updated"
    updated = client.put(f"/books/{book_id}", json=updated_data)
    assert updated.status_code == 200
    assert updated.json()["title"].endswith("Updated")

    deleted = client.delete(f"/books/{book_id}")
    assert deleted.status_code == 200
    assert client.get(f"/books/{book_id}").status_code == 404


def test_duplicate_isbn_is_rejected():
    payload = sample_book()
    assert client.post("/books/", json=payload).status_code == 201
    duplicate = dict(payload, title="Another title")
    response = client.post("/books/", json=duplicate)
    assert response.status_code == 409


def test_validation_and_missing_book():
    invalid = dict(sample_book(), publication_year=500)
    assert client.post("/books/", json=invalid).status_code == 422
    assert client.get("/books/99999").status_code == 404
