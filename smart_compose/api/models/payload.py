from typing import List

from pydantic import BaseModel


class SentimentPayload(BaseModel):
    text: str


def payload_to_list(payload: SentimentPayload) -> List:
    return [payload.text]
