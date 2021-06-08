from dependency_injector import containers, providers

from backend.sevices.service_calculator import CalculatorService, Operation2params
from .sevices.Calculator import Calculator


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    operation = providers.Factory(
        Operation2params,
        x=config.x,
        y=config.y,
    )

    calculate = providers.Factory(
        CalculatorService,
        operation=operation,
    )
