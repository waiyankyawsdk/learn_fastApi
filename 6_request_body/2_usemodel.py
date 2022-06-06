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


@app.post("/items/")
#declare its type as the model you created Item
async def create_item(item: Item):
    item_dict = item.dict()
    #dict() : create a dictionary
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict
