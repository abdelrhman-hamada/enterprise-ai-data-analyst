from pydantic import BaseModel
from typing import List , Dict , Any , Optional

class ChartConfig (BaseModel) :
    chart_type : str 
    title : str 

    x_axis : Optional[str] = None
    y_axis : Optional[str] = None 

class ChartResponse (BaseModel) :
    config : ChartConfig
    data : Dict[str,Any]