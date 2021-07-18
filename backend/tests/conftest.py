import asyncio
import pytest
from fastapi import FastAPI

from app.clients.db import DBClient
from app.api.v1 import nodes, healthcheck, cache

app = FastAPI()


@pytest.fixture()
def test_app():
    @app.on_event("startup")
    async def startup():
        loop = asyncio.get_event_loop()
        app.db = DBClient({}, loop=loop)

    app.include_router(nodes.router)
    app.include_router(cache.router)
    app.include_router(healthcheck.router)
    return app
