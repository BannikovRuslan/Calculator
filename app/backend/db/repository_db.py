from datetime import datetime
from backend.db.resource_db import OperationTypes, OperationsInTime


class DBRepository:

    def __init__(self, session_factory):
        self.session_factory = session_factory
        self.session = session_factory()

    def addOperationType(self, operation_type: str) -> None:
        self.session.add(OperationTypes(operationtype=operation_type))
        self.session.commit()

    def addSingleData(self, operation: str) -> None:
        id_operation_type = self.getOperationTypeID(operation_type=operation)
        now = datetime.now()
        new_operation = OperationsInTime(operation=id_operation_type, time=now)
        self.session.add(new_operation)
        self.session.commit()

    def getOperationTypeID(self, operation_type: str) -> int:
        query = self.session.query(OperationTypes).filter(OperationTypes.operationtype == operation_type).first()
        return query.id_operationtype

