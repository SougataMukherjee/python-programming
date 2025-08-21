import pytest
from python.my_fetch import fetch_sync


class DummyResponse:
    def __init__(self, json_data):
        self._json_data = json_data

    def json(self):
        return self._json_data

def test_fetch_sync(monkeypatch):
    def mock_get(url):
        return DummyResponse({"id": 1, "title": "test"})

    # ✅ correct patch path: <module>.<object>
    monkeypatch.setattr("python.me_fetch.requests.get", mock_get)

    result = fetch_sync("https://fakeurl.com")  # ✅ just call the function
    assert result["id"] == 1
    assert result["title"] == "test"
