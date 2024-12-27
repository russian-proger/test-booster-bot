""" Main File """

from os import environ

from telegram.ext import ApplicationBuilder

from .command_handlers import init_commands
from .callbacks import init_callbacks
from .message_handlers import init_message_handlers

def serve():
    """ Start serving """
    application = ApplicationBuilder().token(environ['TELEGRAM_TOKEN']).build()

    init_commands(application)
    init_callbacks(application)
    init_message_handlers(application)

    application.run_polling()
