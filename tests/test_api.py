"""
Integration tests for the FastAPI application (app/main.py).
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestHealthEndpoint:
    """Tests for GET /health."""

    def test_health_returns_200(self):
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_response_body(self):
        response = client.get("/health")
        assert response.json() == {"status": "ok"}


# TODO: class TestSimulateReviewEndpoint:
#     def test_simulate_review_returns_200(self): ...
#     def test_simulate_review_response_schema(self): ...
#     def test_simulate_review_unknown_user_returns_404(self): ...

# TODO: class TestUserProfileEndpoint:
#     def test_get_profile_returns_200(self): ...
#     def test_get_profile_unknown_user_returns_404(self): ...
