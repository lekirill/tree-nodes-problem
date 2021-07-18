import os

DB_SETTINGS = {
    'dsn': os.getenv('DB_URL') or 'postgresql://user:pswrd@0.0.0.0:5432/nodes',
    'max_size': os.getenv('DB_POOL_MAXSIZE') or 5,
    'min_size': os.getenv('DB_POOL_MINSIZE') or 1,
}
