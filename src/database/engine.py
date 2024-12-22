""" Module for establishing connection with PostgreSQL """

from os import environ

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

from ..utils.singleton import singleton

@singleton
def get_engine() -> Engine:
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

def dispose_engine():
    """ Close connection """
    get_engine().dispose()

def create_session() -> Session:
    """ Return new session """
    return Session(bind=get_engine())
