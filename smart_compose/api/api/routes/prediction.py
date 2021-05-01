from starlette.requests import Request
from fastapi import APIRouter, Depends

from smart_compose.api.services.models import SentimentModel
from smart_compose.api.models.payload import SentimentPayload
from smart_compose.api.models.prediction import SentimentPredictionResult

router = APIRouter()


@router.post("/predict_sentiment", response_model=SentimentPayload,
             name="predict_sentiment")
def post_predict(
    request: Request,
    authenticated: bool = Depends(validate_request),
    block_data: SentimentPayload = None
) -> SentimentPredictionResult:
    if not authenticated:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail=AUTH_REQ,
            headers={})

    model: SentimentModel = request.app.state.model
    prediction: SentimentPredictionResult = model.predict(block_data)

    return prediction
