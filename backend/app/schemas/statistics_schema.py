from pydantic import BaseModel
from typing import Dict , Any 

class StatisticsReport (BaseModel) :
    mean : Dict[str , float]
    median : Dict [str , float]
    std : Dict [str ,float]
    mode : Dict[str,Any]
    variance : Dict[str , float]
    minimum : Dict[str , float]
    maximum : Dict[str , float]


