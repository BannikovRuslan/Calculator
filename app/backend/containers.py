from dependency_injector import containers, providers

from backend.sevices.RandomGenerator import RandomGenerator


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    data = providers.Factory(
        RandomGenerator,
        a=config.a,
        b=config.b,
    )

    generator = providers.Factory(
        RandomGenerator.generate,
        count=config.count
    )
