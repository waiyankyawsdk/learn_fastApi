from fastapi import FastAPI

app = FastAPI() #get instance of fastAPI

# can declare path "parameters" or "variable" with the same syntax of Python format strings
@app.get("/items/{item_id}")
#The value of path parameter item_id will be passed as argument item_id
async def readitem(item_id):
    return {"item_id" : item_id}
#output : {"item_id":"foo"}


