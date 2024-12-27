""" Main File """

from os import environ

from telegram.ext import ApplicationBuilder

from .commands import init_commands
from .callbacks import init_callbacks

def serve():
    """ Start serving """
    application = ApplicationBuilder().token(environ['TELEGRAM_TOKEN']).build()

    init_commands(application)
    init_callbacks(application)

    application.run_polling()
