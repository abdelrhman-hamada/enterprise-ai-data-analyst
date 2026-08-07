from fastapi import APIRouter, UploadFile, File
import os
from app.services.file_service import read_file , load_dataframe , save_uploaded_file
from app.schemas.file_scheme import DatasetSummary
from app.services.cleaning_service import analyze_cleaning , detect_outlier
from app.schemas.cleaning_schema import CleaningReport , OutlierReport
from app.schemas.statistics_schema import StatisticsReport
from app.services.statistics_service import generate_statistics
from app.schemas.correlation_schema import CorrelationReport
from app.services.correlation_service import analyze_correlation

router = APIRouter(prefix="/api", tags=["Data"])


@router.get("/")
def home():
    return {"message": "API is working!!"}


@router.post("/upload",response_model=DatasetSummary)
async def upload_file(file: UploadFile = File(...)):
    file_path = await save_uploaded_file(file)
    result = read_file(file_path)
    return result

@router.post("/clean",response_model=CleaningReport)
async def clean_dataset (file : UploadFile = File(...)) :
    file_path = await save_uploaded_file(file)
    df = load_dataframe(file_path)
    result = analyze_cleaning(df)
    return result

@router.post ("/statistics",response_model=StatisticsReport)
async def statistics (file : UploadFile = File(...)) :
        file_path = await save_uploaded_file(file)
        df = load_dataframe(file_path)
        result = generate_statistics(df)
        return result

@router.post("/outlier",response_model=OutlierReport) 
async def detect_dataset_outliers (file : UploadFile = File(...) ) :
     file_path = await save_uploaded_file(file)
     df = load_dataframe(file_path)
     return detect_outlier(df)


@router.post("/correlation", response_model=CorrelationReport)
async def correlation_analysis(file: UploadFile = File(...)):

    file_path = await save_uploaded_file(file)

    df = load_dataframe(file_path)

    result = analyze_correlation(df)

    return result