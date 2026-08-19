from fastapi import APIRouter, UploadFile, File
import os
from app.services.file_service import read_file , load_dataframe , save_uploaded_file
from app.services.cleaning_service import analyze_cleaning 
from app.schemas.cleaning_schema import CleaningReport 
from app.schemas.dataset_report_schema import DatasetReport
from app.services.report_service import generate_report


router = APIRouter(prefix="/api", tags=["Data"])


@router.get("/")
def home():
    return {"message": "API is working!!"}



@router.post("/clean",response_model=CleaningReport)
async def clean_dataset (file : UploadFile = File(...)) :
    file_path = await save_uploaded_file(file)
    df = load_dataframe(file_path)
    result = analyze_cleaning(df)
    return result

@router.post("/report", response_model=DatasetReport)
async def dataset_report(file: UploadFile = File(...)):
    file_path = await save_uploaded_file(file)
    df = load_dataframe(file_path)
    result = generate_report(df)
    return result

