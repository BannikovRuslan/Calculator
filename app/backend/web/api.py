from dependency_injector.wiring import Provide

from backend.sevices.Calculator import Calculator
from fastapi import FastAPI, Depends
from backend.containers import Container
from backend.sevices.RandomGenerator import RandomGenerator

app = FastAPI()


@app.put("/calculate/plus")
def calculate_plus(x: float, y: float):
    calculator = Calculator()
    return {"x": x, "y": y, "result:": calculator.plus(x, y)}


@app.put("/calculator/minus")
def calculate_minus(x: float, y: float):
    calculator = Calculator()
    return {"x": x, "y": y, "result:": calculator.minus(x, y)}


@app.put("/random/range")
def random_range(n: int, generator: RandomGenerator = Depends(Provide[Container.generator])):
    random_list = generator.generate(n)
    return {"result:": random_list}
