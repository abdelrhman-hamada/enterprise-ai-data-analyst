from fastapi import APIRouter, UploadFile, File
import os
from app.services.file_service import read_file , load_dataframe , save_uploaded_file
from app.services.cleaning_service import analyze_cleaning 
from app.schemas.cleaning_schema import CleaningReport 
from app.schemas.dataset_report_schema import DatasetReport
from app.services.report_service import generate_report
from app.services.chart_service import generate_histogram,generate_bar_chart,generate_boxplot,generate_correlation_heatmap , recommend_charts
from app.schemas.chart_schema import ChartResponse , ChartRecommendationResponse



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

@router.post("/charts/histogram", response_model=ChartResponse)
async def histogram_chart(
    file: UploadFile = File(...),
    column: str = ""
):
    file_path = await save_uploaded_file(file)

    df = load_dataframe(file_path)

    return generate_histogram(df, column)

@router.post("/charts/bar", response_model=ChartResponse)
async def bar_chart(
    file: UploadFile = File(...),
    column: str = ""
):
    file_path = await save_uploaded_file(file)

    df = load_dataframe(file_path)

    return generate_bar_chart(df, column)

@router.post("/charts/boxplot", response_model=ChartResponse)
async def boxplot_chart(
    file: UploadFile = File(...),
    column: str = ""
):
    file_path = await save_uploaded_file(file)

    df = load_dataframe(file_path)

    return generate_boxplot(df, column)

@router.post("/charts/heatmap", response_model=ChartResponse)
async def heatmap_chart(
    file: UploadFile = File(...)
):
    file_path = await save_uploaded_file(file)

    df = load_dataframe(file_path)

    return generate_correlation_heatmap(df)

@router.post(
    "/charts/recommendations",
    response_model=ChartRecommendationResponse
)
async def chart_recommendations(
    file: UploadFile = File(...)
):

    file_path = await save_uploaded_file(file)

    df = load_dataframe(file_path)

    return recommend_charts(df)