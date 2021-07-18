import os

SERVICE_PORT = int(os.getenv('SERVICE_PORT', 8000))
SERVICE_HOST = os.getenv('SERVICE_HOST', '0.0.0.0')
DEBUG = os.getenv('DEBUG', 'false')
