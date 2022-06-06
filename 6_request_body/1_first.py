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
    return item

#same as declaring query para, default value of model attribute is not required. Use None to make optional
# JSON "object" or Python "dict"
# {
#     "name": "Foo",
#     "description": "An optional description",
#     "price": 45.2,
#     "tax": 3.5
# }

# {
#     "name": "Foo",
#     "price": 45.2
# }


