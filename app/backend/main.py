import uvicorn
from fastapi import FastAPI

from backend.db.containers_db import DBContainer
from backend.sevices.containers import Container, CalcContainer
from backend.sevices import Calculator
from backend.web import api

if __name__ == '__main__':
    parameters = {"a": -10, "b": 10}

    container = Container()
    container.config.from_dict(parameters)
    container.wire(modules=[api])

    calc_container = CalcContainer()
    calc_container.wire(modules=[api])

    db_container = DBContainer()
    db_params = {"path": "d://operations.db"}
    db_container.config.from_dict(db_params)
    db_container.wire(modules=[api, Calculator])

    app_container = FastAPI()
    app_container.include_router(api.router)

    uvicorn.run(app_container, host="0.0.0.0", port=8000)
