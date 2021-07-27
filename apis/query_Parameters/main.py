from fastapi import FastAPI
from typing import Optional

app = FastAPI()

fake_items_db = [{'item_name': 'Foo'}, {'item_name': 'Bar'}, {'item_name': 'Baz'}]


# @app.get('/items/')
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip:skip + limit]

# @app.get('/items/')
# async def read_item(item_id: str, q: Optional[str] = None):
#     if q:
#         return {'item_id': item_id, 'q': q}
#     return {'item_id': item_id}

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: str, item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, 'owner_id': user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
