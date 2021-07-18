import uvicorn
from app.main import app

from settings import general


if __name__ == '__main__':
    uvicorn.run(app,
                host=general.SERVICE_HOST,
                port=general.SERVICE_PORT,
                debug=general.DEBUG,
                forwarded_allow_ips='*')
