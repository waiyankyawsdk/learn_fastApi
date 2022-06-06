from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")

#declare optional query parameters, by default to None
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id" : item_id}
    if q:
        item.update({"q" : q})
    if not short:
        item.update(
            {"description" : "This is an amazing item that has a long description"}
        )
    return item

#q'll be optional,and will be None by default
#http://127.0.0.1:8000/items/foo?short=1
#http://127.0.0.1:8000/items/foo?short=True
#http://127.0.0.1:8000/items/foo?short=true
#http://127.0.0.1:8000/items/foo?short=on
#http://127.0.0.1:8000/items/foo?short=yes
#http://127.0.0.1:8000/items/foo?short=false
