""" Messages """

from pathlib import Path

from telegram import Bot
from telegram import InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram import KeyboardButton
from telegram.constants import ParseMode
from telegram import BotCommand
from telegram import BotCommandScopeChat

from ..gigachat.generator import generate_message
from ..utils.file import read_text


class Message:
    text: str
    markup: InlineKeyboardMarkup|ReplyKeyboardMarkup|ReplyKeyboardRemove|None

    def __init__(self, text, markup=None):
        self.text = text
        self.markup = markup
