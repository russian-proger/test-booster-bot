""" Entrypoint """

import asyncio
from pathlib import Path

from .bot.server import serve
from .database.base import Base
from .database.engine import get_engine, dispose_engine
from .utils.env import load_env

def main():
    """ Main function """

    # Load environment
    try:
        load_env(Path(__file__).parent.parent / Path('.env'))
    except FileNotFoundError as e:
        print("❌ Environment wasn't found")
        raise e
    else:
        print("✅ Environment was loaded")

    # Connect to PostgreSQL
    try:
        engine = get_engine()
    except Exception as e:
        print("❌ Connection couldn't has been established")
        raise e
    else:
        print("✅ Connection with PostgreSQL was established")

    # Create tables
    try:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
    except Exception as e:
        print("❌ Couldn't update the scheme")
        raise e
    else:
        print("✅ Scheme was updated")

    # Start serving telegram events
    try:
        print("🚀 Server is running")
        serve()
        print("\n🏁 Server was stopped")
    except Exception as e:
        print("❌ Couldn't start server")
        raise e

    # Disconnect from PostgreSQL
    try:
        dispose_engine()
    except Exception as e:
        print("❌ Couldn't dispose engine")
        raise e
    else:
        print("🏁 Connection with PostgreSQL was closed")

if __name__ == '__main__':
    main()
