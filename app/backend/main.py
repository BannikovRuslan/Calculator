import uvicorn
from fastapi import FastAPI

from backend.containers import Container
from backend.web import api

app = FastAPI()

if __name__ == '__main__':
    parameters = {"a": -10, "b": 10}

    container = Container()
    container.config.from_dict(parameters)
    container.wire(modules=[api])

    app_container = FastAPI()
    app_container.container = container
    app_container.include_router(api.router)

    uvicorn.run(app, host="0.0.0.0", port=8000)
