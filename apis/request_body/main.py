from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict


# @app.put('/items/{item_id}')
# async def edit_item(item_id: int, item: Item):
#     return {'item_id': item_id, **item.dict()}

# Request body + path + query parameters
@app.put('/items/{item_id}')
async def edit_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {'item_id': item_id, **item.dict()}
    if q:
        result.update({'q': q})
    return result
