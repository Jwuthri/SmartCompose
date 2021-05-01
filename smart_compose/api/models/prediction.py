from typing import Dict

from pydantic import BaseModel


class SentimentPredictionResult(BaseModel):
    sentiment: str
    suggestion: Dict[str, float]
    duration: float = 0.0
