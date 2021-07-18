from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix='/v1/healthcheck'
)


@router.get("/ping")
async def get_node(request: Request):
    """
    Ping just check if database is reachable
    :param request:
    :return:
    """
    await request.app.db.first("SELECT 1", ())
    return JSONResponse(
        status_code=200,
        content={'message': 'pong'}
    )
