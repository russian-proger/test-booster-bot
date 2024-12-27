""" Messages """

from telegram import InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

class Message:
    text: str
    markup: InlineKeyboardMarkup|ReplyKeyboardMarkup|ReplyKeyboardRemove|None

    def __init__(self, text, markup=None):
        self.text = text
        self.markup = markup
