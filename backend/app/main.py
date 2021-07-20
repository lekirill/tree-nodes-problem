import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import nodes, healthcheck, cache
from app.clients import setup
from app.exceptions import database

logger = logging.getLogger("uvicorn")


def create_app() -> FastAPI:
    application = FastAPI()
    origins = [
        "*",
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:3007",
    ]

    @application.on_event("startup")
    async def startup_event():
        try:
            await setup.setup(application)
        except database.NoDBConnectionException as e:
            logger.error(e.msg)
            return

            # set tree_cache:
        application.tree_cache = {}
        # set counter node_id for new nodes:
        application.temp_node_id_counter = 0

    @application.on_event("shutdown")
    async def shutdown_event():
        await setup.shutdown(application)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    application.include_router(nodes.router)
    application.include_router(cache.router)
    application.include_router(healthcheck.router)
    return application


app = create_app()
