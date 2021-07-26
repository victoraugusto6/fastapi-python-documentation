from fastapi.testclient import TestClient

from fastAPI.main_1 import app

client = TestClient(app)


def test_read_root():
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.json() == {'Hello': 'World'}


def test_read_item():
    resp = client.get('/items/1')
    response = resp.json()
    assert response['item_id'] == 1
    resp = client.get('/items/1?q=Teste')
    response = resp.json()
    assert response['item_id'] == 1
    assert response['q'] == 'Teste'
