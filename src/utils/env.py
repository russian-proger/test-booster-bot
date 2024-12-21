""" Working with local environment """

from pathlib import Path
from dotenv import load_dotenv

def load_env(dotenv_path: Path):
    """ Load `.env` """

    if dotenv_path.exists():
        load_dotenv(dotenv_path)
    else:
        raise FileNotFoundError("Not found .env")
