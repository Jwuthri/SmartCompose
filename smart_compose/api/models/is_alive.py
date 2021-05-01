from pydantic import BaseModel


class IsAliveResult(BaseModel):
    is_alive: bool
