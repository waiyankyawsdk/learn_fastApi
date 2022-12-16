from typing import Union

from fastapi import FastAPI, Query  #import Query

app = FastAPI()

#default value , min_length, max_length, regex, 

@app.get("/items/")
async def read_items(
    q: Union[str, None] = Query(
        default="fixedquery", min_length=3, max_length=50, regex="^fixedquery$"
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
