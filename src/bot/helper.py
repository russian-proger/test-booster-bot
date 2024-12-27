""" Helper functions """

from pathlib import Path
from typing import List

from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes

from .services.user import get_user_by_update
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

def handle_context(user_context: str):
    """ Decorator """
    def wrap(message_handler):
        async def wrapping_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
            user = get_user_by_update(update)
            if user and user.context == user_context:
                await message_handler(update, context)
        return wrapping_handler
    return wrap

def handle_contexts(user_contexts: List[str]):
    """ Decorator """
    def wrap(message_handler):
        async def wrapping_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
            user = get_user_by_update(update)
            if user and user.context in user_contexts:
                await message_handler(update, context)
        return wrapping_handler
    return wrap
