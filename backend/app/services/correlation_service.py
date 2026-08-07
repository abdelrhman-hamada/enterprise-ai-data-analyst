import pandas as pd


def analyze_correlation(df: pd.DataFrame):

    numeric_df = df.select_dtypes(include="number")

    correlation_matrix = numeric_df.corr()

    matrix = correlation_matrix.round(3).to_dict()

    strong_correlations = []
    weak_correlations = []

    columns = correlation_matrix.columns

    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):

            column_1 = columns[i]
            column_2 = columns[j]

            correlation = correlation_matrix.loc[column_1, column_2]

            if pd.isna(correlation):
                continue

            correlation = float(correlation)

            item = {
                "column_1": column_1,
                "column_2": column_2,
                "correlation": correlation
            }

            if abs(correlation) >= 0.7:
                strong_correlations.append(item)

            elif abs(correlation) < 0.3:
                weak_correlations.append(item)

    return {
        "matrix": matrix,
        "strong_correlations": strong_correlations,
        "weak_correlations": weak_correlations
    }