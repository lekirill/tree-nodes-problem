from fastapi.testclient import TestClient


def test_ping(monkeypatch, test_app):
    async def first(query, params):
        return [(1,)]

    with TestClient(test_app) as client:
        monkeypatch.setattr(test_app.db, 'first', first, raising=True)
        response = client.get(
            'v1/healthcheck/ping',
        )
        assert response.status_code == 200
