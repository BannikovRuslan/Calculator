from datetime import datetime

from dependency_injector.wiring import Provide, inject

from backend.sevices.Calculator import Calculator
from fastapi import Depends, APIRouter
from backend.sevices.containers import Container, CalcContainer
from backend.sevices.RandomGenerator import RandomGenerator

router = APIRouter()


@router.put("/calculate/plus")
@inject
def calculate_plus(x: float, y: float, calculator: Calculator = Depends(Provide[CalcContainer.calculator])):
    return {"x": x, "y": y, "result:": calculator.plus(x, y)}


@router.put("/calculator/minus")
@inject
def calculate_minus(x: float, y: float, calculator: Calculator = Depends(Provide[CalcContainer.calculator])):
    return {"x": x, "y": y, "result:": calculator.minus(x, y)}


@router.put("/random/range")
@inject
def random_range(n: int, generator: RandomGenerator = Depends(Provide[Container.generator])):
    return {"x": n, "result:": generator.generate(n)}


@router.get("/operations/time_interval")
def get_operations_time_interval(start: datetime, finish: datetime):
    return {"start": start, "finish": finish}
