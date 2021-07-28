from enum import Enum
from fastapi import FastAPI

app = FastAPI()


class ModelName(str, Enum):
    victor = 'Victor Augusto'
    larissa = 'Larissa Zandonadi'


@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name.value == ModelName.victor:
        return {'model_name': model_name, 'message': 'Acessado Victor A.'}
    if model_name == ModelName.larissa:
        return {'model_name': model_name, 'message': 'Acessado Larissa Z.'}
