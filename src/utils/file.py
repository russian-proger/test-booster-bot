""" Utility for easy reading file """

from pathlib import Path

def read_text(path: Path|str) -> str:
    """ Return file content """
    with open(path, 'r', encoding='utf-8') as f:
        return ''.join(f.readlines())
