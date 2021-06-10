from dependency_injector.wiring import Provide, inject

from backend.db.repository_db import DBRepository
from backend.sevices.Calculator import Calculator
from fastapi import Depends, APIRouter
from backend.containers import Container, CalcContainer, DBContainer
from backend.sevices.RandomGenerator import RandomGenerator

router = APIRouter()


@router.put("/calculate/plus")
@inject
def calculate_plus(x: float, y: float,
                   calculator: Calculator = Depends(Provide[CalcContainer.calculator]),
                   db_repository: DBRepository = Depends(Provide[DBContainer.db_repository])):
    db_repository.add_operation_in_time(operation="сложение")
    return {"x": x, "y": y, "result:": calculator.plus(x, y)}


@router.put("/calculator/minus")
@inject
def calculate_minus(x: float, y: float, calculator: Calculator = Depends(Provide[CalcContainer.calculator])):
    return {"x": x, "y": y, "result:": calculator.minus(x, y)}


@router.put("/random/range")
@inject
def random_range(n: int, generator: RandomGenerator = Depends(Provide[Container.generator])):
    random_list = generator.generate(n)
    return {"result:": random_list}
