from fastapi import FastAPI, File, UploadFile

from typing import Union

app = FastAPI()


@app.post("/files/")
async def create_file(file: Union[bytes, None] = File(default=None)):
    if not file:
        return {"message":"No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: Union[UploadFile,None] = None):
    if not file:
        return {"message":"No upload fine sent"}
    else:
        return {"filename": file.filename}
