from pydantic import BaseModel
from typing import List , Dict

class CleaningReport (BaseModel) :
    missing_values : Dict[str , int]
    duplicates : int
    recommended_fill : Dict [str , str]
    recommended_drop : list [str]
    recommended_type_conversion : Dict [str , str]

class OutlierReport (BaseModel) :
    outlier_counts : Dict[str , int]
    outlier_indices : Dict[str , List[int]]