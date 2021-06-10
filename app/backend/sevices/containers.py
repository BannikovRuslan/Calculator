from dependency_injector import containers, providers

from backend.sevices.Calculator import Calculator
from backend.sevices.RandomGenerator import RandomGenerator


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(strict=True)

    generator = providers.Factory(
        RandomGenerator,
        a=config.a,
        b=config.b,
    )


class CalcContainer(containers.DeclarativeContainer):
    config = providers.Configuration(strict=True)

    calculator = providers.Factory(
        Calculator,
    )


