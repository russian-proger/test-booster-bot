""" Entrypoint """

from pathlib import Path

from .bot.server import serve
from .database.engine import get_engine, dispose_engine
from .utils.env import load_env

def main():
    """ Main function """

    # Load environment
    load_env(Path(__file__).parent.parent / Path('.env'))

    # Connect to PostgreSQL
    get_engine()

    # Start serving telegram events
    serve()

    # Disconnect from PostgreSQL
    dispose_engine()

if __name__ == '__main__':
    main()
