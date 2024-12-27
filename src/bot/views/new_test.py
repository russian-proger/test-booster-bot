""" New test message """

from telegram import ReplyKeyboardRemove

from ..message import Message

def generate_greeting_msg(**kwargs) -> Message:
    return Message(
        "Введите название нового теста\:",
        ReplyKeyboardRemove()
    )
