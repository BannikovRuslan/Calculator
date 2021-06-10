import traceback
from datetime import datetime

from dependency_injector.wiring import Provide, inject
from fastapi import Depends

from backend.db.containers_db import DBContainer
from backend.db.repository_db import DBRepository


class Calculator:

    def __init__(self): pass

    @staticmethod
    @inject
    def plus(x: float, y: float, db_repository: DBRepository = Depends(Provide[DBContainer.db_repository])) -> float:
        s = x + y
        time = datetime.now()
        db_repository.add_operation_in_time(operation="сложение", operation_time=time)
        return s

    @staticmethod
    @inject
    def minus(x: float, y: float, db_repository: DBRepository = Depends(Provide[DBContainer.db_repository])) -> float:
        d = x - y
        time = datetime.now()
        db_repository.add_operation_in_time(operation="вычитание", operation_time=time)
        return d