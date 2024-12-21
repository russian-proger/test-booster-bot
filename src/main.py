""" Entrypoint """

from pathlib import Path

from .bot.server import serve
from .database.connection import close_connection, get_connection
from .utils.env import load_env

def main():
    """ Main function """

    # Load environment
    load_env(Path(__file__).parent.parent / Path('.env'))

    # Connect to PostgreSQL
    get_connection()

    # Start serving telegram events
    serve()

    # Disconnect from PostgreSQL
    close_connection()

if __name__ == '__main__':
    main()
