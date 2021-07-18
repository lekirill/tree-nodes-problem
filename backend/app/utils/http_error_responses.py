from fastapi.responses import JSONResponse


def _error_response_base(code, msg=None):
    return JSONResponse(
        status_code=code,
        content={'success': False, 'error': msg}
    )


def node_id_absence(msg='Bad request'):
    code = 400
    return _error_response_base(code, msg)


def db_error(msg=None):
    code = 503
    return _error_response_base(code, f'No connection to db: {msg}')
