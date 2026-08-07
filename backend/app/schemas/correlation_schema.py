from pydantic import BaseModel
from typing import Dict, List


class CorrelationItem(BaseModel):
    column_1: str
    column_2: str
    correlation: float


class CorrelationReport(BaseModel):
    matrix: Dict[str, Dict[str, float]]

    strong_correlations: List[CorrelationItem]

    weak_correlations: List[CorrelationItem]