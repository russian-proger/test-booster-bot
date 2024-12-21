""" Module for establishing connection with PostgreSQL """

from os import environ

from sqlalchemy import Engine, create_engine

from ..utils.singleton import singleton

@singleton
def get_connection() -> Engine:
    """ Return connection with database """
    credentials = [
        environ['POSTGRESQL_USER'],
        environ['POSTGRESQL_PASS'],
        environ['POSTGRESQL_HOST'],
        environ['POSTGRESQL_PORT'],
        environ['POSTGRESQL_DATABASE']
    ]

    uri = 'postgresql://{}:{}@{}:{}/{}'.format(*credentials)

    return create_engine(uri)

def close_connection():
    """ Close connection """
    get_connection().dispose()
