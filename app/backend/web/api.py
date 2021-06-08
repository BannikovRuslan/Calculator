from backend.sevices.service_calculator import CalculatorService
from fastapi import FastAPI
from backend.containers import Container

app = FastAPI()


@app.put("/calculate/plus")
def calculate_plus(x: float, y: float):
    container = Container()
    container.config.x = x
    container.config.y = y
    calculate = container.operation()
    return {"x": x, "y": y, "result:": calculate.plus()}


@app.put("/calculator/minus")
def calculate_minus(x: float, y: float):
    container = Container()
    container.config.x = x
    container.config.y = y
    calculate = container.operation()
    return {"x": x, "y": y, "result:": calculate.minus()}
