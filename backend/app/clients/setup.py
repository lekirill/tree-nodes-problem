import asyncio

from .db import DBClient
from app.exceptions import database

from settings import db


async def setup(app):
    loop = asyncio.get_event_loop()
    app.db = DBClient(db.DB_SETTINGS, loop=loop)
    try:
        await app.db.setup()
    except Exception:
        raise database.NoDBConnectionException(db.DB_SETTINGS["dsn"])



async def shutdown(app):
    await app.db.close()
