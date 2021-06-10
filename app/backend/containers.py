from dependency_injector import containers, providers

from backend.db.repository_db import DBRepository
from backend.db.resource_db import DBResource
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


class DBContainer(containers.DeclarativeContainer):

    config = providers.Configuration(strict=True)

    resource = providers.Resource(
        DBResource,
        path=config.path,
    )
