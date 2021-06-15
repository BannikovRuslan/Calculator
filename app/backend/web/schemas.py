from datetime import datetime

from pydantic import BaseModel


class CalculatorData(BaseModel):
    x: float
    y: float


class RandomInterval(BaseModel):
    a: int
    b: int


class OperationsData(BaseModel):
    data: datetime
    operation: str
