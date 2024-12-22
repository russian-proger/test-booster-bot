""" Messages """

from pathlib import Path

from telegram import Bot
from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton

from ..gigachat.generator import generate_message
from ..utils.file import read_text

TEMPLATE_FOLDER = Path(__file__).parent / 'templates'

def get_template(filename: str):
    """ Read and return template file content """
    return read_text(TEMPLATE_FOLDER / filename)

MSG_START_TESTING = "Начать тестирование!"
PROMPT_ERROR_ANSWER = get_template('prompt_error_answer.txt')

async def send_greeting(bot: Bot, chat_id: int|str):
    """ Send greeting message """

    greeting_message = get_template('greeting.txt')

    markup = ReplyKeyboardMarkup([[KeyboardButton(MSG_START_TESTING)]], True)

    await bot.send_message(
        chat_id=chat_id,
        text=greeting_message,
        reply_markup=markup,
    )

async def send_message(bot: Bot, chat_id: int|str, message: str):
    """ Send custom message to chat_id """
    await bot.send_message(
        chat_id=chat_id,
        text=message,
    )

async def send_ai_message(
        bot: Bot,
        chat_id: int|str,
        system_prompt: str|None,
        user_prompt: str|None):

    """ Send message from GigaChat by prompts """
    await bot.send_message(
        chat_id=chat_id,
        text=generate_message(system_prompt, user_prompt),
    )
