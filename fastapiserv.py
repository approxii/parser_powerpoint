from fastapi import FastAPI, UploadFile, File
from fastapi.exceptions import HTTPException
from typing import Annotated
from fastapi.responses import FileResponse
import uvicorn
import json

app = FastAPI()


@app.get("/")
def read_root():
  return {"Hello": "FastAPI"}

@app.post("/file/upload")
def upload_file(file: UploadFile):
    if file.content_type != "application/json":
        raise HTTPExceptionError(400, detail="Invalid document type")
    else:
        data = json.load(file.file.read())
    return {"content":data ,"filename":file.filename}

if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1", port=8000)