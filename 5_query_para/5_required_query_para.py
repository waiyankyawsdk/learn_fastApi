from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")

#needy is required parameter of str
async def read_user_item(item_id: str, needy: str):
    item = {"item_id" : item_id, "needy" : needy}
    return item

#http://127.0.0.1:8000/items/foo-item
#http://127.0.0.1:8000/items/foo-item?needy=sooneedy
#