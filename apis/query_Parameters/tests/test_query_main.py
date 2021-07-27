import pytest
from httpx import AsyncClient

from apis.query_Parameters.main import app, fake_items_db


@pytest.mark.asyncio
async def test_read_item_interval(skip=0, limit=10):
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get('/items/')
    assert response.status_code == 200
    assert response.json() == fake_items_db[skip:skip + limit]


@pytest.mark.asyncio
async def test_read_item(user_id: str = 1, item_id: str = 1, q: str = None, short: bool = False):
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get(f'/users/{user_id}/items/{item_id}')
    assert response.status_code == 200
    assert response.json() == {
        'item_id': '1',
        'owner_id': '1',
        'description': 'This is an amazing item that has a long description'
    }
