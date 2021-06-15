from datetime import datetime
from typing import List

from pydantic import BaseModel


class CalculatorData(BaseModel):
    x: float
    y: float


class RandomInterval(BaseModel):
    a: int
    b: int


class OperationData(BaseModel):
    data: datetime
    operation: str


class OperationsInterval(BaseModel):
    start: datetime
    finish: datetime


class OperationsData(BaseModel):
    interval: OperationsInterval
    operations: List[OperationData]