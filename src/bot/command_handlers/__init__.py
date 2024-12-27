from telegram.ext import Application
from telegram.ext import CommandHandler

from .mytests import handle_mytests_cmd
from .newtest import handle_newtest_cmd
from .start import handle_start_cmd

def init_commands(app: Application):
    app.add_handlers([
        CommandHandler('mytests', handle_mytests_cmd),
        CommandHandler('newtest', handle_newtest_cmd),
        CommandHandler('start', handle_start_cmd),
    ])
