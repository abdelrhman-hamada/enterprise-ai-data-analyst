from fastapi import APIRouter, UploadFile, File
import os
from app.services.file_service import read_file
from app.schemas.file_scheme import DatasetSummary

router = APIRouter(prefix="/api", tags=["Data"])


@router.get("/")
def home():
    return {"message": "API is working!!"}


@router.post("/upload",response_model=DatasetSummary)
async def upload_file(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads",file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    result = read_file(file_path)

    return result