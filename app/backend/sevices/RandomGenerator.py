import random
from datetime import datetime

from dependency_injector.wiring import Provide, inject
from fastapi import Depends

from backend.db.containers_db import DBContainer
from backend.db.repository_db import DBRepository


class RandomGenerator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    @inject
    def generate(self, count: int, db_repository: DBRepository = Depends(Provide[DBContainer.db_repository])) -> object:
        try:
            numbers = []
            for i in range(count):
                numbers.append(random.randrange(self.a, self.b - 1))
        except Exception:
            print('Что-то случилось с генератором случаных чисел!')
            return None
        else:
            time = datetime.now()
            db_repository.add_operation_in_time(operation="генерация случайных чисел", operation_time=time)
            return numbers
