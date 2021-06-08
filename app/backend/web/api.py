from dependency_injector.wiring import Provide

from backend.sevices.Calculator import Calculator
from fastapi import Depends, APIRouter
from backend.containers import Container
from backend.sevices.RandomGenerator import RandomGenerator

router = APIRouter()


@router.put("/calculate/plus")
def calculate_plus(x: float, y: float):
    calculator = Calculator()
    return {"x": x, "y": y, "result:": calculator.plus(x, y)}


@router.put("/calculator/minus")
def calculate_minus(x: float, y: float):
    calculator = Calculator()
    return {"x": x, "y": y, "result:": calculator.minus(x, y)}


@router.put("/random/range")
def random_range(n: int, generator: RandomGenerator = Depends(Provide[Container.generator])):
    random_list = generator.generate(n)
    return {"result:": random_list}
