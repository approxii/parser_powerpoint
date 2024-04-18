from fastapi.exceptions import HTTPException
from typing import Annotated
from fastapi.responses import FileResponse, Response
import uvicorn
from io import BytesIO
from updater import parser as Service
from depends import get_service

app = FastAPI()


@app.get("/")
def read_root():
  return {"Hello": "FastAPI"}

@app.post("/update")
async def upload(file: UploadFile = File(...),
    service: Service = Depends(get_service),
):
    contents = await file.read()
    service.load(BytesIO(contents))
    service.update()
    new_file = service.save_to_bytes()
    headers = {
        "Content-Disposition": f"attachment; filename={file.filename}",
    }
    media_type = "application/vnd.ms-powerpoint"

    return Response(content=new_file.getvalue(), headers=headers, media_type=media_type)


if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1", port=8000)
