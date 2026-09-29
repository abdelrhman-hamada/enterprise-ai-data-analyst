from pydantic import BaseModel
from typing import List


class ChartConfig(BaseModel):
    chart_type: str
    title: str
    x_axis: str | None = None
    y_axis: str | None = None


class ChartResponse(BaseModel):
    config: ChartConfig
    data: dict


class ChartRecommendation(BaseModel):
    chart_type: str
    column: str | None = None
    reason: str


class ChartRecommendationResponse(BaseModel):
    recommendations: List[ChartRecommendation]