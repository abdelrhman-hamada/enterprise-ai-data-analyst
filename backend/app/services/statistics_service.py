import pandas as pd 

def generate_statistics (df : pd. DataFrame) :
    numirac_df = df.select_dtypes(include="number")

    if numirac_df.empty :
        return{
                "mean" : {},
                "median" : {},
                "std" : {},
                "mode" : {},
                "variance" : {},
                "minimum" : {},
                "maximum" : {}
        }
    else :
        return {
                "mean" : numirac_df.mean().to_dict() ,
                "median" : numirac_df.median().to_dict() ,
                "std" : numirac_df.std().to_dict() ,
                "mode" : numirac_df.mode().iloc[0].to_dict() ,
                "variance" : numirac_df.var().to_dict() ,
                "minimum" : numirac_df.min().to_dict() ,
                "maximum" : numirac_df.max().to_dict()           
        }