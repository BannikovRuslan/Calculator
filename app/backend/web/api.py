from backend.sevices.Calculator import Calculator
from fastapi import FastAPI
from backend.containers import Container

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
def random_range(a: int, b: int, n: int):
    container = Container()
    parameters = {"a": a, "b": b, "count": n}
    container.config.from_dict(parameters)
    data = container.data()
    random_list = container.generator()
    return {"a": a, "b": b, "data:": data, "result:": random_list}
