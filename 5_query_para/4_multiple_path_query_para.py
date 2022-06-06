from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/items/{item_id}")

#declare optional query parameters, by default to None
async def read_user_item(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id" : item_id, "owner_id" : user_id}
    if q:
        item.update({"q" : q})
    if not short:
        item.update(
            {"description" : "This is an amazing item that has a long description"}
        )
    return item

#q'll be optional,and will be None by default
