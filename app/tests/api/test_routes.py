import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


@pytest.fixture
def sample_pdf_path():
    return "app/tests/data/sample.pdf"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_upload_pdf(sample_pdf_path):
    with open(sample_pdf_path, "rb") as pdf:
        response = client.post(
            "/api/v1/upload", files={"file": ("sample.pdf", pdf, "application/pdf")}
        )
        assert response.status_code == 200
        result = response.json()
        assert result["status"] == "success"
        assert result["filename"] == "sample.pdf"


def test_query():
    response = client.post(
        "/api/v1/query", json={"question": "What is the main topic?"}
    )
    assert response.status_code == 200
    assert isinstance(response.json()["answer"], str)


def test_search():
    response = client.post("/api/v1/search", params={"query": "test", "k": 2})
    assert response.status_code == 200
    assert "results" in response.json()
