from datetime import datetime
from backend.db.resource_db import OperationTypes, OperationsInTime


class DBRepository:

    def __init__(self, session_factory):
        self.session_factory = session_factory

    def add_operation_type(self, operation_type: str) -> None:
        with self.session_factory() as session:
            session.add(OperationTypes(operation_type=operation_type))
            session.commit()

    def add_operation_in_time(self, operation: str) -> None:
        id_operation_type = self.get_operation_type_id(operation_type=operation)
        now = datetime.now()
        new_operation = OperationsInTime(operation=id_operation_type, time=now)
        with self.session_factory() as session:
            session.add(new_operation)
            session.commit()

    def get_operation_type_id(self, operation_type: str) -> int:
        with self.session_factory() as session:
            query = session.query(OperationTypes).filter(OperationTypes.operation_type == operation_type).first()

        if query is None:
            self.add_operation_type(operation_type)
            with self.session_factory() as session:
                query = session.query(OperationTypes).filter(OperationTypes.operation_type == operation_type).first()

        return query.id_operation_type

