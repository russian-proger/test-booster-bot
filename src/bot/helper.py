""" Helper functions """

from pathlib import Path

from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

from ..utils.file import read_text

TEMPLATE_FOLDER = Path(__file__).parent / 'templates'

def get_template(filename: str):
    """ Read and return template file content """
    return read_text(TEMPLATE_FOLDER / filename)

def build_markup(options=list[str]):
    keyboard = None
    if 3 <= len(options):
        keyboard = [[KeyboardButton(i) for i in options[j:j+2]] for j in range(0, len(options), 2)]
    else:
        keyboard = [[KeyboardButton(i) for i in options]]
    return ReplyKeyboardMarkup(keyboard, True)
