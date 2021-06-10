from dependency_injector import containers, providers

from backend.db.repository_db import DBRepository
from backend.db.resource_db import DBResource


class DBContainer(containers.DeclarativeContainer):

    config = providers.Configuration(strict=True)

    resource = providers.Resource(
        DBResource,
        path=config.path,
    )

    db_repository = providers.Singleton(
        DBRepository,
        session_factory=resource
    )