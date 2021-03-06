from dependency_injector import resources
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import Engine
from sqlalchemy.orm import relationship, Session, sessionmaker

Base = declarative_base()


class OperationTypes(Base):
    __tablename__ = 'operation_types'
    __tableargs__ = {
        'comment': 'Типы выполняемых операций / действий'
    }

    id_operation_type = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    operation_type = Column(
        String(100),
        comment='Тип операции'
    )

    def __repr__(self):
        return f'{self.id_operationtype} {self.operationtype}'


class OperationsInTime(Base):
    __tablename__ = 'operations_in_time'
    __tableargs__ = {
        'comment': 'Выполненные операции / действия во времени'
    }

    id_operation_in_time = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )

    operation = Column(
        Integer,
        ForeignKey('operation_types.id_operation_type'),
        comment='Тип операции'
    )

    time = Column(
        DateTime,
        comment='Время выполнения операции / действия'
    )

    operation_types = relationship(
        'OperationTypes',
        backref='time_type',
        lazy='subquery'
    )


class DBResource(resources.Resource):

    def init(self, path: str):
        engine = create_engine("sqlite:///" + path, echo=True)
        Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=engine)
        return session_factory

    def shutdown(self, engine: Engine) -> None:
        pass


