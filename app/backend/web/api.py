from datetime import datetime

from dependency_injector.wiring import Provide, inject

from backend.db.containers_db import DBContainer
from backend.db.repository_db import DBRepository
from backend.sevices.Calculator import Calculator
from fastapi import Depends, APIRouter, Body, Query
from backend.sevices.containers import Container, CalcContainer
from backend.sevices.RandomGenerator import RandomGenerator
from backend.web.schemas import CalculatorData, RandomInterval, OperationsData, OperationsInterval

router = APIRouter()


@router.put("/calculate/plus")
@inject
def calculate_plus(data: CalculatorData = Body(..., embed=True), calculator: Calculator = Depends(Provide[CalcContainer.calculator])):
    return {"data": data, "result:": calculator.plus(data)}


@router.put("/calculator/minus")
@inject
def calculate_minus(data: CalculatorData, calculator: Calculator = Depends(Provide[CalcContainer.calculator])):
    return {"data": data, "result:": calculator.minus(data)}


@router.put("/random/range")
@inject
def random_range(interval: RandomInterval = Body(..., embed=True), n: int = Body(...),
                 generator: RandomGenerator = Depends(Provide[Container.generator])):

    generator.a = interval.a
    generator.b = interval.b

    result = generator.generate(n)
    return result


@router.get("/operations/time_interval")
@inject
def get_operations_time_interval(data: OperationsData,
                                 db_repository: DBRepository = Depends(Provide[DBContainer.db_repository])):
    result = db_repository.operations_time_interval(data.interval)
    return OperationsData(**result.dict())
