from backend.sevices.Calculator import Calculator


class TestCalculator:

    def test_plus(self):
        a = 3
        b = 4
        calc = Calculator()
        assert 7 == calc.plus(a, b)