import pandas as pd 

def read_file (file_path : str ) :
    if file_path.endswith("csv") :
        df = pd.read_csv(file_path)
    elif file_path.endswith("slsx") :
        df = pd.read_excel(file_path)
    else :
        raise ValueError("unsupported file format")
    return{
        "rows" : len(df),
        "columens" : list(df.columns),
        "dtypes" : df.dtypes.astype("str").to_dict(),
    }
