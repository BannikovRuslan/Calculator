from dependency_injector import resources
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import Engine
from sqlalchemy.orm import relationship, Session

Base = declarative_base()


class OperationTypes(Base):
    __tablename__ = 'operationtypes'
    __tableargs__ = {
        'comment': 'Типы выполняемых операций / действий'
    }

    id_operationtype = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    operationtype = Column(
        String(100),
        comment='Тип операции'
    )

    def __repr__(self):
        return f'{self.id_operationtypes} {self.operationtype}'


class OperationsInTime(Base):
    __tablename__ = 'operationsintime'
    __tableargs__ = {
        'comment': 'Выполненные операции / действия во времени'
    }

    id_operationintime = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )

    operation = Column(
        Integer,
        ForeignKey('operationtypes.id_operationtype'),
        comment='Тип операции'
    )

    time = Column(
        DateTime,
        comment='Время выполнения операции / действия'
    )

    operationtypes = relationship(
        'OperationTypes',
        backref='operation_type',
        lazy='subquery'
    )


class DBResource(resources.Resource):

    def init(self, path: str):
        engine = create_engine("sqlite:///" + path, echo=True)
        Base.metadata.create_all(engine)
        self.addBaseData(engine)
        return engine

    def addBaseData(self, engine: Engine) -> None:
        session = Session(bind=engine)
        operations = [
            OperationTypes(operationtype='сложение'),
            OperationTypes(operationtype='вычитание'),
            OperationTypes(operationtype='генерация случайного числа')
        ]
        session.add_all(operations)

    def shutdown(self, engine: Engine) -> None:
        pass


