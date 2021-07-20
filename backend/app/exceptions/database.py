class NoDBConnectionException(Exception):
    def __init__(self, db_string: str):
        self.msg = f'No connection to database: {db_string.split("@")[1]}. Need to restart APP'
