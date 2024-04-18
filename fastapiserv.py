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

@app.post("/upload")
def upload(file: UploadFile = File("/a.pptx")):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}

if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1", port=8000)
