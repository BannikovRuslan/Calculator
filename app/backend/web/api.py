from backend.sevices.CalculatorService import CalculatorService
from fastapi import FastAPI

app = FastAPI()


@app.put("/calculate/plus/")
def calculate_plus(x: float = 0.0, y: float = 0.0):
    calculator = CalculatorService(x, y)
    return {"x": x, "y": y, "result:": calculator.plus()}


@app.put("/calculator/minus")
def calculate_minus(x: float = 0.0, y: float = 0.0):
    calculator = CalculatorService(x, y)
    return {"x": x, "y": y, "result:": calculator.minus()}
