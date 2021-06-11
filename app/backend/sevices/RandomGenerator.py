import random
from datetime import datetime

from pydantic import BaseModel, ValidationError, Field

from dependency_injector.wiring import Provide, inject
from fastapi import Depends

from backend.db.containers_db import DBContainer
from backend.db.repository_db import DBRepository


class Data(BaseModel):
    n: int = Field(..., gt=0, le=100)

class RandomGenerator:

    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    @inject
    def generate(self, count: int, db_repository: DBRepository = Depends(Provide[DBContainer.db_repository])) -> object:

        try:
            data = Data(
                n=count
            )
            numbers = []
            for i in range(data.n):
                numbers.append(random.randrange(self.a, self.b - 1))
            time = datetime.now()
            db_repository.add_operation_in_time(operation="генерация случайных чисел", operation_time=time)

            return {"n": data.n, "array": numbers}

        except ValidationError as e:
            print(e.json())

            return {"error": "Count of element must be great then 0 and less or equal then 100!"}


