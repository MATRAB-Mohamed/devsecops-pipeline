import json 
from app import app

def test_root_returns_hell_world():
    client = app.test_client()
    res = client.get("/")

    assert res.status_code == 200

    data = json.loads(res.data.decode("utf-8"))
    assert "message" in data
    assert "Hello, World" in data["message"]
