import pandas as pd 

def analyze_cleaning (df : pd.DataFrame) : 
    missing = df.isnull().sum().to_dict()
    duplicates = int(df.duplicated().sum())
    fill = {}
    convert = {}
    drop = []

    for column in df.columns :
        if df[column].isnull().sum() == 0 :
            continue
        elif pd.api.types.is_numeric_dtype(df[column]) :
            fill[column] = "fill with median" 
        else :
            fill[column] = "fill with mode"
    return {
        "missing_values" : missing ,
        "duplicates" : duplicates ,
        "recommended_fill" : fill ,
        "recommended_drop" : drop ,
        "recommended_type_conversion" : convert ,
    }

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