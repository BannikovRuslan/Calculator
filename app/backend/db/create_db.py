from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Text, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import os

if os.path.exists("operations.db"):
    os.remove("operations.db")

engine = create_engine("sqlite:///operations.db", echo=True)

Base = declarative_base()  # может из другого модуля?


class OperationTypes(Base):
    __tablename__ = 'operationtypes'
    __tableargs__ = {
        'comment': 'Типы выполняемых операций / действий'
    }

    id_operationtypes = Column(
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
        ForeignKey('operationtypes.id_operationtypes'),
        comment='Тип операции'
    )
    operation_rs = relationship(
        'operationtypes',
        backref='operation_type',
        lazu='subquery'
    )

    time = Column(
        DateTime,
        comment='Время выполнения операции / действия'
    )


Base.metadata.create_all(engine)
