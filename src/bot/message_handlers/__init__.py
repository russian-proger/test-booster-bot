from telegram.ext import Application
from telegram.ext import MessageHandler

from .new_test import handle_new_test_msg

def init_message_handlers(app: Application):
    app.add_handlers([
        MessageHandler(None, handle_new_test_msg),
    ])
