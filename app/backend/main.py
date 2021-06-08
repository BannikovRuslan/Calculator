
import uvicorn
from fastapi import FastAPI

from backend.containers import Container
from backend.sevices import RandomGenerator
from backend.web import api
from backend.web.api import app

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

    parameters = {"a": -10, "b": 10}

    container = Container()
    container.config.from_dict(parameters)
    container.wire(modules=[api])

    app = FastAPI()
    app.container = container
    app.include_router(api.app)