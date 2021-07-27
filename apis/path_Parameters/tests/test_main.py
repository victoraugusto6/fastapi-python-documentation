import pytest
from httpx import AsyncClient

from apis.path_Parameters.main import app, ModelName


@pytest.mark.asyncio
async def test_read_item(item_id=1):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f'/items/{item_id}')
    assert response.status_code == 200
    assert response.json() == {'item_id': 1}


@pytest.mark.asyncio
async def test_get_model_first(model_name=ModelName.victor):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f'/models/{model_name}')
    assert response.status_code == 200
    assert response.json() == {'model_name': model_name, 'message': 'Acessado Victor A.'}


@pytest.mark.asyncio
async def test_get_second(model_name=ModelName.larissa):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f'/models/{model_name}')
    assert response.status_code == 200
    assert response.json() == {'model_name': model_name, 'message': 'Acessado Larissa Z.'}
