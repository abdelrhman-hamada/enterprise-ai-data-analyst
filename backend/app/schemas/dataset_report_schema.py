from pydantic import BaseModel
from typing import List, Dict, Any

from app.schemas.statistics_schema import StatisticsReport
from app.schemas.outlier_schema import OutlierReport
from app.schemas.correlation_schema import CorrelationReport

"///////////////////////////////////////////////////////////////////////////////"

class DatasetOverview(BaseModel):
    rows: int
    columns_count: int
    memory_usage_mb: float

    numeric_count: int
    categorical_count: int
    datetime_count: int

"////////////////////////////////////////////////////////////////////////////"
class ColumnProfile(BaseModel):
    dtype: str

    unique_count: int
    unique_percentage: float

    missing_count: int
    missing_percentage: float

    quality_status: str

"///////////////////////////////////////////////////////////////////////////"
class DataQuality(BaseModel):
    missing_values: Dict[str, int]
    missing_percentage: Dict[str, float]

    duplicates: int
    duplicates_percentage: float

    quality_status: str

"////////////////////////////////////////////////////////////////////////"
class NumericalAnalysis(BaseModel):
    columns: List[str]
    statistics: StatisticsReport

"/////////////////////////////////////////////////////////////////////////////////"
class CategoricalAnalysis(BaseModel):
    columns: List[str]
    unique_counts: Dict[str, int]
    most_frequent: Dict[str, Any]

"////////////////////////////////////////////////////////////////////////////////"

class DatasetReport(BaseModel):
    overview: DatasetOverview
    data_quality: DataQuality
    column_profiles: Dict[str, ColumnProfile]
    numerical_analysis: NumericalAnalysis
    categorical_analysis: CategoricalAnalysis
    outliers: OutlierReport
    correlations: CorrelationReport













