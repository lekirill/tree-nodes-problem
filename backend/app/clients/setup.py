import asyncio

from .db import DBClient

from settings import db


async def setup(app):
    loop = asyncio.get_event_loop()
    app.db = DBClient(db.DB_SETTINGS, loop=loop)
    await app.db.setup()


async def shutdown(app):
    await app.db.close()
