""" Main File """

from os import environ

from telegram import Update
from telegram.ext import ApplicationBuilder
from telegram.ext import CommandHandler
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler
from telegram.ext.filters import TEXT

from .messages import send_greeting
from .messages import send_new_test
from .services.start import add_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ `start` command handler """
    if update.effective_chat is not None:
        await send_greeting(context.bot, update.effective_chat.id)
        add_user(update)

async def create_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ `start` command handler """
    if update.effective_chat is not None:
        await send_new_test(context.bot, update.effective_chat.id)

async def handle_message(_update: Update, _context: ContextTypes.DEFAULT_TYPE):
    """ Message handler """
    # print(update)
    # print(update.callback_query)

def serve():
    """ Start serving """
    application = ApplicationBuilder().token(environ['TELEGRAM_TOKEN']).build()

    start_handler = CommandHandler('start', start)
    new_test_handler = CommandHandler('newtest', create_test)

    application.add_handler(start_handler)
    application.add_handler(new_test_handler)
    application.add_handler(MessageHandler(TEXT, handle_message))

    application.run_polling()
