from datetime import datetime

from dependency_injector.wiring import inject, Provide, Closing
from sqlalchemy.orm import sessionmaker, Session

from backend.containers import DBContainer
from backend.db.create_db import OperationTypes, OperationsInTime


class DBRepository:

    def __init__(self):
        pass

    @inject
    def addSingleData(self, operation: str, engine: DBContainer = Closing(Provide[DBContainer.resource])) -> None:
        session = Session(bind=engine)
        id_operation_type = self.getOperationTypeID(operation_type="'"+operation+"'")
        now = datetime.now()
        new_operation = OperationsInTime(operation="'"+id_operation_type+"'", time="'"+now+"'")
        session.add(new_operation)
        session.commit()

    @inject
    def getOperationTypeID(self,
                           operation_type: str,
                           engine: DBContainer = Closing(Provide[DBContainer.resource])) -> int:
        session = Session(bind=engine)
        query = session.query(OperationTypes).filter(OperationTypes.operationtype == operation_type).first()
        return query

