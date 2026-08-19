import pandas as pd

from app.services.statistics_service import generate_statistics
from app.services.correlation_service import analyze_correlation
from app.services.outlier_service import detect_outlier


def generate_report(df: pd.DataFrame):

    numeric_columns = df.select_dtypes(include=["number"]).columns.to_list()
    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns.to_list()
    datetime_columns = df.select_dtypes(
        include=["datetime"]
    ).columns.to_list()

    # OVERVIEW
    rows = len(df)
    columns_count = len(df.columns)

    memory_usage_mb = round(
        df.memory_usage(deep=True).sum() / (1024 ** 2),
        2
    )

    overview = {
        "rows": rows,
        "columns_count": columns_count,
        "memory_usage_mb": memory_usage_mb,
        "numeric_count": len(numeric_columns),
        "categorical_count": len(categorical_columns),
        "datetime_count": len(datetime_columns)
    }

    # DATA QUALITY
    missing_values = df.isnull().sum().to_dict()

    missing_percentage = (
        (df.isnull().sum() / rows) * 100
    ).round(2).to_dict() if rows > 0 else {
        column: 0.0 for column in df.columns
    }

    duplicates = int(df.duplicated().sum())

    duplicates_percentage = (
        round((duplicates / rows) * 100, 2)
        if rows > 0
        else 0.0
    )

    total_missing = df.isnull().sum().sum()

    if total_missing == 0 and duplicates == 0:
        quality_status = "Good"

    elif duplicates_percentage > 10 or (
        rows > 0
        and columns_count > 0
        and (total_missing / (rows * columns_count)) * 100 > 20
    ):
        quality_status = "Poor"

    else:
        quality_status = "Warning"

    data_quality = {
        "missing_values": missing_values,
        "missing_percentage": missing_percentage,
        "duplicates": duplicates,
        "duplicates_percentage": duplicates_percentage,
        "quality_status": quality_status
    }

    # COLUMN PROFILE
    column_profiles = {}

    for column in df.columns:

        missing_count = int(df[column].isnull().sum())

        missing_percentage_value = (
            round((missing_count / rows) * 100, 2)
            if rows > 0
            else 0.0
        )

        unique_count = int(
            df[column].nunique(dropna=True)
        )

        unique_percentage = (
            round((unique_count / rows) * 100, 2)
            if rows > 0
            else 0.0
        )

        if missing_percentage_value == 0:
            column_quality = "Good"

        elif missing_percentage_value > 50:
            column_quality = "Poor"

        else:
            column_quality = "Warning"

        column_profiles[column] = {
            "dtype": str(df[column].dtype),
            "unique_count": unique_count,
            "unique_percentage": unique_percentage,
            "missing_count": missing_count,
            "missing_percentage": missing_percentage_value,
            "quality_status": column_quality
        }

    # NUMERICAL ANALYSIS
    statistics = generate_statistics(df)

    numerical_analysis = {
        "columns": numeric_columns,
        "statistics": statistics
    }

    # CATEGORICAL ANALYSIS
    unique_counts = {}
    most_frequent = {}

    for column in categorical_columns:

        unique_counts[column] = int(
            df[column].nunique(dropna=True)
        )

        mode = df[column].mode()

        if not mode.empty:
            most_frequent[column] = mode.iloc[0]

        else:
            most_frequent[column] = None

    categorical_analysis = {
        "columns": categorical_columns,
        "unique_counts": unique_counts,
        "most_frequent": most_frequent
    }

    # OUTLIERS AND CORRELATIONS
    outliers = detect_outlier(df)
    correlations = analyze_correlation(df)

    return {
        "overview": overview,
        "data_quality": data_quality,
        "column_profiles": column_profiles,
        "numerical_analysis": numerical_analysis,
        "categorical_analysis": categorical_analysis,
        "outliers": outliers,
        "correlations": correlations
    }


