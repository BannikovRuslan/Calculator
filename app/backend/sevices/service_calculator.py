class Operation:

    def __init__(self): pass


class Operation2params(Operation):

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def plus(self) -> float:
        return self.x + self.y


class CalculatorService:

    def __init__(self, operation: Operation):
        self.operation = operation

    def plus(self, x: float, y: float) -> float:
        return x + y

    def minus(self, x, y):
        return x - y
