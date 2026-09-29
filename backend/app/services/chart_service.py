import pandas as pd
import numpy as np


def generate_histogram(df: pd.DataFrame, column: str):

    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found")

    if not pd.api.types.is_numeric_dtype(df[column]):
        raise ValueError(f"Column '{column}' must be numeric")

    values = df[column].dropna()

    if values.empty:
        raise ValueError(f"Column '{column}' has no valid values")

    counts, bins = np.histogram(values, bins=10)

    return {
        "config": {
            "chart_type": "histogram",
            "title": f"{column} Distribution",
            "x_axis": column,
            "y_axis": "Count"
        },
        "data": {
            "bins": [float(value) for value in bins],
            "counts": [int(value) for value in counts]
        }
    }


def generate_bar_chart(df: pd.DataFrame, column: str):

    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found")

    values = df[column].dropna()

    if values.empty:
        raise ValueError(f"Column '{column}' has no valid values")

    counts = values.value_counts().head(10)

    return {
        "config": {
            "chart_type": "bar",
            "title": f"{column} Distribution",
            "x_axis": column,
            "y_axis": "Count"
        },
        "data": {
            "labels": [str(value) for value in counts.index],
            "values": [int(value) for value in counts.values]
        }
    }


def generate_boxplot(df: pd.DataFrame, column: str):

    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found")

    if not pd.api.types.is_numeric_dtype(df[column]):
        raise ValueError(f"Column '{column}' must be numeric")

    values = df[column].dropna()

    if values.empty:
        raise ValueError(f"Column '{column}' has no valid values")

    return {
        "config": {
            "chart_type": "boxplot",
            "title": f"{column} Box Plot",
            "x_axis": column
        },
        "data": {
            "column": column,
            "min": float(values.min()),
            "q1": float(values.quantile(0.25)),
            "median": float(values.median()),
            "q3": float(values.quantile(0.75)),
            "max": float(values.max())
        }
    }


def generate_correlation_heatmap(df: pd.DataFrame):

    numeric_df = df.select_dtypes(include=["number"])

    if numeric_df.empty:
        raise ValueError("Dataset has no numeric columns")

    correlation = numeric_df.corr()

    return {
        "config": {
            "chart_type": "heatmap",
            "title": "Correlation Matrix"
        },
        "data": {
            "columns": correlation.columns.tolist(),
            "matrix": correlation.round(3).fillna(0).values.tolist()
        }
    }

def recommend_charts(df: pd.DataFrame):
    
    recommendations = []

    numeric_columns = df.select_dtypes(
        include=["number"]
    ).columns.tolist()

    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    # Numeric columns
    for column in numeric_columns:

        recommendations.append({
            "chart_type": "histogram",
            "column": column,
            "reason": "Numeric column - useful for analyzing data distribution"
        })

        recommendations.append({
            "chart_type": "boxplot",
            "column": column,
            "reason": "Numeric column - useful for detecting outliers"
        })

    # Categorical columns
    for column in categorical_columns:

        unique_count = df[column].nunique(dropna=True)

        if unique_count <= 10:

            recommendations.append({
                "chart_type": "bar",
                "column": column,
                "reason": "Low-cardinality categorical column"
            })

    # Correlation
    if len(numeric_columns) >= 2:

        recommendations.append({
            "chart_type": "heatmap",
            "column": None,
            "reason": "Multiple numeric columns are available for correlation analysis"
        })

    return {
        "recommendations": recommendations
    }