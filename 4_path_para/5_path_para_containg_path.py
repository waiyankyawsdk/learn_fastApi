from fastapi import FastAPI

app = FastAPI()

#declare a path parameter containg a path
#parameter name = file_path, :path = says that the parameter should match any path
@app.get("/file/{file_path:path}")

async def read_file(file_path: str):
    return {"file_path" : file_path}