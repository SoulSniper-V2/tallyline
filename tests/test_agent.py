from fastapi.testclient import TestClient

from app.agent import provider_label
from app.main import app


def test_provider_label_distinguishes_offline_and_live_paths(monkeypatch):
    monkeypatch.delenv("TALLYLINE_AGENT_MODE", raising=False)
    monkeypatch.delenv("TALLYLINE_MODEL_PROVIDER", raising=False)
    assert provider_label() == "Strands • offline evidence pass"

    monkeypatch.setenv("TALLYLINE_AGENT_MODE", "live")
    monkeypatch.setenv("TALLYLINE_MODEL_PROVIDER", "gemini")
    assert provider_label() == "Strands • live gemini"


def test_live_route_fails_closed_without_provider_credentials(monkeypatch):
    monkeypatch.setenv("TALLYLINE_AGENT_MODE", "live")
    monkeypatch.setenv("TALLYLINE_MODEL_PROVIDER", "gemini")
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)

    response = TestClient(app).post("/api/run")

    assert response.status_code == 503
    assert "Gemini live mode needs" in response.json()["detail"]
