from datetime import datetime

from sqlalchemy.dialects.sqlite import json

from backend.db.resource_db import OperationTypes, OperationsInTime


class DBRepository:

    def __init__(self, session_factory):
        self.session_factory = session_factory

    def add_operation_type(self, operation_type: str) -> None:
        with self.session_factory() as session:
            session.add(OperationTypes(operation_type=operation_type))
            session.commit()

    def add_operation_in_time(self, operation: str, operation_time: datetime) -> None:
        with self.session_factory() as session:
            id_operation_type = self._get_operation_type_id(operation_type=operation, session=session)

            if id_operation_type is None:
                self.add_operation_type(operation)
                id_operation_type = self._get_operation_type_id(operation_type=operation, session=session)
                if id_operation_type is None:
                    print("Не удалось найти операцию!")
                    return

            new_operation = OperationsInTime(operation=id_operation_type, time=operation_time)
            session.add(new_operation)
            session.commit()

    def _get_operation_type_id(self, operation_type: str, session) -> int:
        query = session.query(OperationTypes).filter(OperationTypes.operation_type == operation_type).first()
        if query is None:
            return None
        else:
            return query.id_operation_type

    def operations_time_interval(self, start: datetime, finish: datetime):
        with self.session_factory() as session:
            query = session.query(OperationsInTime.time, OperationTypes.operation_type)\
                .join(OperationTypes)\
                .filter(OperationsInTime.time >= start)\
                .filter(OperationsInTime.time <= finish).all()
        if query is None:
            return None
        else:
            return query
