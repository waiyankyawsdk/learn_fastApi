from typing import Union

from fastapi import FastAPI

#import BaseModel from pydantic
from pydantic import BaseModel

#declare your data model as a class that inherits from BaseModel
class Item(BaseModel):
    name : str
    description : Union[str, None] = None
    price : float
    tax : Union[float, None] = None

app = FastAPI()


@app.put("/items/{item_id}")
#declare path parameters and request body at the same time.
async def create_item(item_id : int, item: Item):
    return {"item_id": item_id, **item_dict()}
