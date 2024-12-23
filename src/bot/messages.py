""" Messages """

from pathlib import Path

from telegram import Bot
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram import KeyboardButton
from telegram.constants import ParseMode

from ..gigachat.generator import generate_message
from ..utils.file import read_text

TEMPLATE_FOLDER = Path(__file__).parent / 'templates'

def get_template(filename: str):
    """ Read and return template file content """
    return read_text(TEMPLATE_FOLDER / filename)

MSG_TASK_1_OPTIONS = ["log()", "print()", "write()", "out()"]
MSG_TASK_1_ANSWER = MSG_TASK_1_OPTIONS[1]

MSG_TASK_2_OPTIONS = ["Hi, name", "Ошибка", "Hi, John", "Hi, "]
MSG_TASK_2_ANSWER = MSG_TASK_2_OPTIONS[2]

MSG_TASK_3_OPTIONS = ["Ошибка", "0", "11", "10", "23"]
MSG_TASK_3_ANSWER = MSG_TASK_3_OPTIONS[2]

MSG_TASK_4_OPTIONS = ["Найдено", "Готово", "Ошибка"]
MSG_TASK_4_ANSWER = MSG_TASK_4_OPTIONS[0]

MSG_START_TESTING = "Начать тестирование!"
MSG_SKIP_TASK = "Пропустить задание"
PROMPT_ERROR_START_ANSWER = get_template('prompt_error_start_answer.txt')
PROMPT_ERROR_INCORRECT_OPTION = get_template('prompt_error_incorrect_option.txt')

def buildMarkup(options=list[str]):
    keyboard = None
    if 3 <= len(options):
        keyboard = [[KeyboardButton(i) for i in options[j:j+2]] for j in range(0, len(options), 2)]
    else:
        keyboard = [[KeyboardButton(i) for i in options]]
    return ReplyKeyboardMarkup(keyboard, True)

async def send_greeting(bot: Bot, chat_id: int|str):
    """ Send greeting message """

    greeting_message = get_template('greeting.txt')

    markup = ReplyKeyboardMarkup([[KeyboardButton(MSG_START_TESTING)]], True)

    await bot.send_message(
        chat_id=chat_id,
        text=greeting_message,
        parse_mode=ParseMode.MARKDOWN_V2,
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

async def send_feedback(
        bot: Bot,
        chat_id: int|str,
        verdict: bool):
    message: str
    if verdict:
        message = get_template('correct_answer.txt')
    else:
        message = get_template('wrong_answer.txt')
    await bot.sendMessage(chat_id, message, reply_markup=ReplyKeyboardRemove())

async def send_task_1(bot: Bot, chat_id: int|str):
    markup = buildMarkup(MSG_TASK_1_OPTIONS)
    await bot.sendMessage(chat_id, '⚡️')
    await bot.sendMessage(chat_id, get_template('task_1.txt'), ParseMode.MARKDOWN_V2, reply_markup=markup)

async def send_task_2(bot: Bot, chat_id: int|str):
    markup = buildMarkup(MSG_TASK_2_OPTIONS)
    await bot.sendMessage(chat_id, get_template('task_2.txt'), ParseMode.MARKDOWN_V2, reply_markup=markup)

async def send_task_3(bot: Bot, chat_id: int|str):
    markup = buildMarkup(MSG_TASK_3_OPTIONS)
    await bot.sendMessage(chat_id, get_template('task_3.txt'), ParseMode.MARKDOWN_V2, reply_markup=markup)

async def send_task_4(bot: Bot, chat_id: int|str):
    markup = buildMarkup(MSG_TASK_4_OPTIONS)
    await bot.sendMessage(chat_id, get_template('task_4.txt'), ParseMode.MARKDOWN_V2, reply_markup=markup)

async def send_task_5(bot: Bot, chat_id: int|str):
    markup = ReplyKeyboardMarkup([[KeyboardButton(MSG_SKIP_TASK)]], True)
    await bot.sendMessage(chat_id, get_template('task_5.txt'), ParseMode.MARKDOWN_V2, reply_markup=markup)

async def send_finish(bot: Bot, chat_id: int|str):
    await bot.sendMessage(chat_id, get_template('finish.txt'), reply_markup=ReplyKeyboardRemove())
