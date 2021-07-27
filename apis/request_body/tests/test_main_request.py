import pytest
from httpx import AsyncClient

from apis.request_body.main import app


@pytest.mark.asyncio
async def test_create_item():
    data = {
        "name": "Foo",
        "description": "An optional description",
        "price": 1,
        "tax": 1
    }

    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.post('/items/', json=data)
    assert response.status_code == 200
    data.update({"price_with_tax": 2.0})
    assert response.json() == data


@pytest.mark.asyncio
async def test_edit_item(item_id=1, q='Teste'):
    data = {
        "name": "string",
        "description": "string",
        "price": 0.0,
        "tax": 0.0
    }
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.put(f'/items/{item_id}?q={q}', json=data)
    assert response.status_code == 200
    data.update({'item_id': item_id})
    data.update({'q': q})
    assert response.json() == data
