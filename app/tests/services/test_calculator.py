import pytest

from backend.db.containers_db import DBContainer
from backend.db.repository_db import DBRepository
from backend.sevices.Calculator import Calculator
from backend.web.schemas import CalculatorData


class TestCalculator:

    @pytest.fixture
    def db_repository(self):
        db_container = DBContainer()
        db_params = {"path": "d://op.db"}
        db_container.config.from_dict(db_params)
        return db_container.db_repository()

    @pytest.fixture
    def calc(self, db_repository):
        return Calculator(db_repository=db_repository)

    def test_plus(self, calc):
        a = 3
        b = 4
        data = CalculatorData(x=3, y=4)
        assert 7 == calc.plus(data=data)
