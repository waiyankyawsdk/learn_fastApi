# can define some parameters as required, 
# some as having a default value, and some entirely optional
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")

#needy: required str, skip: int with default value 0, limit: opitional int
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
