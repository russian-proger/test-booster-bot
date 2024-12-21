""" Entrypoint """

from pathlib import Path

from .utils.env import load_env
from .bot.server import serve

if __name__ == '__main__':
    load_env(Path(__file__).parent.parent / Path('.env'))
    serve()
