""" Main File """

import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

def singleton(func):
    """ Make the only one instance """
    instance = None
    def getInstance(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = func()
        return instance
    return getInstance

@singleton
def get_llm() -> GigaChat:
    """ Create instance of GigaChat """
    return GigaChat(
        credentials=os.environ['GIGACHAT_AUTH_KEY'],
        scope=os.environ['GIGACHAT_SCOPE'],
        model='GigaChat',
        verify_ssl_certs=False,
        streaming=False,
    )

def generate_start_message():
    """ Generate greeting message """
    messages = [
        SystemMessage(content="Ты телеграм бот для проведения онлайн тестирования"),
        HumanMessage(content="Привет! Кто ты и чем ты мне можешь помочь?")
    ]
    res = get_llm().invoke(messages)
    return res.content


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ `start` command handler """

    if update.effective_chat is not None:
        message = generate_start_message()
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

if __name__ == '__main__':
    dotenv_path = Path(__file__).parent / Path('.env')

    if dotenv_path.exists():
        load_dotenv(dotenv_path)
    else:
        raise FileNotFoundError("Not found .env")

    application = ApplicationBuilder().token(os.environ['TELEGRAM_TOKEN']).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()
