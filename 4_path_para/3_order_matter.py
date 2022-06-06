from fastapi import FastAPI

app = FastAPI()

#get data about the current user
@app.get("/users/me")
async def read_user_me():
    return {"user_id" : "the current user"}

#get data about a specific user by some user ID
@app.get("/users/{user_id}")
async def read_user(user_id:str):
    return {"user_id" : user_id}

#cannot redefine a path operation
# @app.get("/users")
# async def read_users():
#     return ["Rick", "Morty"]


# @app.get("/users")
# async def read_users2():
#     return ["Bean", "Elfo"]
# Note : first one will always use since the path matches first.