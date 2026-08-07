import pandas as pd 
from app.schemas.file_scheme import DatasetSummary
import os
from fastapi import UploadFile

def load_dataframe (file_path : str ) -> pd.DataFrame :
    if file_path.endswith(".csv") :
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx") :
        return pd.read_excel(file_path)
    else :
        raise ValueError("unsupported file format")


    
def read_file (file_path : str ) :
    df = load_dataframe(file_path)
    rows = len(df)
    columns_count = len(df.columns)
    columns = list(df.columns)
    dtypes = df.dtypes.astype("str").to_dict()
    missing_values = df.isnull().sum().to_dict()
    duplicates = int(df.duplicated().sum())
    memory_usage_mb = round(df.memory_usage(deep=True).sum() / (1024 * 1024),2)
    preview = df.head().to_dict(orient="records")
    numric_df = df.select_dtypes(include="number")
    numeric_summary = {}
    for column in numric_df.columns :
        numeric_summary[column]= {
            "count" : float(numric_df[column].count()),
            "mean" : float(numric_df[column].mean()),
            "std" : float(numric_df[column].std()),
            "min" : float(numric_df[column].min()),
            "max" : float(numric_df[column].max())
        }
    return DatasetSummary(
    rows=rows,
    columns_count=columns_count,
    columns=columns,
    dtypes=dtypes,
    missing_values=missing_values,
    duplicates=duplicates,
    memory_usage_mb=memory_usage_mb,
    numeric_summary=numeric_summary,
    preview=preview
    )




async def save_uploaded_file (file : UploadFile) -> str :
    os.makedirs("uploads" , exist_ok=True)
    file_path = os.path.join("uploads",file.filename)
    with open(file_path , "wb") as buffer :
        buffer.write(await file.read())
    return file_path