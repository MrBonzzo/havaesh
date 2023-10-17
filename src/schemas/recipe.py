from typing import TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")


class Response(BaseModel):
    code: int
    status: str
    message: str
    result: Optional[T] = None
