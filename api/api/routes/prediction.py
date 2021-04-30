from starlette.requests import Request
from fastapi import APIRouter, Depends

from api.core.security import *
from api.services.models import SentimentModel
from api.models.payload import SentimentPayload
from api.models.prediction import SentimentPredictionResult

router = APIRouter()


@router.post("/predict_sentiment", response_model=SentimentPayload, name="predict_sentiment")
def post_predict(
    request: Request,
    authenticated: bool = Depends(validate_request),
    block_data: SentimentPayload = None
) -> SentimentPredictionResult:
    if not authenticated:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail=AUTH_REQ, headers={})

    model: SentimentModel = request.app.state.model
    prediction: SentimentPredictionResult = model.predict(block_data)

    return prediction
