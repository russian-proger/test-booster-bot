""" Messages """

from pathlib import Path

from telegram import Bot
from telegram import BotCommandScopeChat
from telegram import ReplyKeyboardRemove

from ..utils.file import read_text

async def send_greeting(bot: Bot, chat_id: int|str):
    """ Send greeting message """

    await bot.delete_my_commands(BotCommandScopeChat(chat_id))

    message_path = Path(__file__).parent / 'templates' / 'greeting.txt'
    greeting_message = read_text(message_path)

    await bot.send_message(
        chat_id=chat_id,
        text=greeting_message,
        reply_markup=ReplyKeyboardRemove(),
    )

async def send_new_test(bot: Bot, chat_id: int|str):
    """ Custom handler """
    await bot.send_message(
        chat_id=chat_id,
        text="Клавиатура обновлена"
    )
