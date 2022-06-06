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
#declare body, path and query parameters, all at the same time
#path is also declared in path, it'll be used as path parametr
#parameter is of a singular type(int,float,str,bool), will be interpreted as a query parameter
#parameter is declared to be of type of Pydantic model, will be interpreted as request body
async def create_item(item_id : int, item: Item, q: Union[str, None] = None):
    result = {"item_id" : item_id, 'abc':item.dict()}
    if q:
        result.update({"q": q})
    return result
