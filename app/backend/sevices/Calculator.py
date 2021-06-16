import traceback
from datetime import datetime

from dependency_injector.wiring import Provide, inject
from fastapi import Depends

from backend.db.containers_db import DBContainer
from backend.db.repository_db import DBRepository
from backend.web.schemas import CalculatorData


class Calculator:

    def __init__(self, db_repository: DBRepository):
        self.db_repository = db_repository

    def plus(self, data: CalculatorData) -> float:
        s = data.x + data.y
        time = datetime.now()
        self.db_repository.add_operation_in_time(operation="сложение", operation_time=time)
        return s

    def minus(self, data: CalculatorData) -> float:
        d = data.x - data.y
        time = datetime.now()
        self.db_repository.add_operation_in_time(operation="вычитание", operation_time=time)
        return d