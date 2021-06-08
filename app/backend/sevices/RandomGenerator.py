import random
from typing import List


class RandomGenerator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def generate(self, count: int) -> object:
        numbers = []
        for i in range(count):
            numbers.append(random.randrange(self.a, self.b - 1))

        return numbers
