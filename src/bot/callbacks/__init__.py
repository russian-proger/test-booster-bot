from telegram.ext import Application
from telegram.ext import CallbackQueryHandler

from .list_my_tests import handle_list_my_tests_clb
from .show_my_test import handle_show_my_test_clb

def init_callbacks(app: Application):
    app.add_handlers([
        CallbackQueryHandler(handle_show_my_test_clb, '^show_my_test:\d+$'),
        CallbackQueryHandler(handle_list_my_tests_clb, '^list_my_tests$'),
    ])
