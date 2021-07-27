from fastapi.testclient import TestClient

from apis.fastAPI.main_2 import app

client = TestClient(app)


def test_read_root():
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.json() == {"Hello": "World"}


def test_read_item(item_id=1, q: int = None):
    resp = client.get(f'/items/{item_id}')
    assert resp.status_code == 200
    assert resp.json() == {"item_id": item_id, "q": q}


def test_update_item(item_id=1):
    resp = client.put(f'/items/{item_id}', json={
        "name": "string",
        "price": 1,
        "is_offer": True
    })
    assert resp.status_code == 200
    assert resp.json() == {"item_price": 1.0, "item_id": item_id}
