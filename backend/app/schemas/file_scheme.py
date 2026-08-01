from pydantic import BaseModel
from typing import Dict, List, Any

class ColumnSummary(BaseModel):
    count: float
    mean: float
    std: float
    min: float
    max: float


class DatasetSummary(BaseModel):
    rows: int
    columns_count: int

    columns: List[str]

    dtypes: Dict[str, str]

    missing_values: Dict[str, int]

    duplicates: int

    memory_usage_mb: float

    numeric_summary: Dict[str, ColumnSummary]

    preview: List[Dict[str, Any]]