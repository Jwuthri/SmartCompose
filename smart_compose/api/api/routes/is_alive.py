from fastapi import APIRouter

from smart_compose.api.models.is_alive import IsAliveResult

router = APIRouter()


@router.get("/is_alive", response_model=IsAliveResult, name="is_alive")
def is_alive() -> IsAliveResult:
    return IsAliveResult(is_alive=True)
