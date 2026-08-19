import pandas as pd

def detect_outlier (df : pd.DataFrame) :
    outlier_counts = {}
    outlier_indices = {}
    numeric_cols = df.select_dtypes(include="number")
    for col in numeric_cols :
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1 

        lower = q1 - 1.5 *  iqr
        upper = q3 + 1.5 * iqr 

        mask = (df[col]<lower) | (df[col]>upper)
        outlier_counts[col] = int(mask.sum())
        outlier_indices[col] = df[mask].index.to_list()

    return {

        "outlier_counts" : outlier_counts ,
        "outlier_indices" : outlier_indices ,
    }