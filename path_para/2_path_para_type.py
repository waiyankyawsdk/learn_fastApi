from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
# can declare the type of a path parameter in the function, using standard Python type annotations
#item_id is declared to be an int
async def readitem(item_id : int):
    return {"item_id" : iWtem_id}
#output : {"item_id":3}

#All the data validation is performed under the hood by Pydantic.
