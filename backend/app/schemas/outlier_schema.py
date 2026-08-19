from pydantic import BaseModel
from typing import List , Dict

class OutlierReport (BaseModel) :
    outlier_counts : Dict[str , int]
    outlier_indices : Dict[str , List[int]]