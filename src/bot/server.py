""" Main File """

import time
from os import environ

from telegram import Update
from telegram.ext import ApplicationBuilder
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext.filters import TEXT
from telegram.ext.filters import Document

from ..utils.constants import FOLDER_DOWNLOADS

from .messages import send_ai_message
from .messages import send_feedback
from .messages import send_task_1
from .messages import send_task_2
from .messages import send_task_3
from .messages import send_task_4
from .messages import send_task_5
from .messages import send_finish
from .messages import MSG_TASK_1_ANSWER
from .messages import MSG_TASK_1_OPTIONS
from .messages import MSG_TASK_2_ANSWER
from .messages import MSG_TASK_2_OPTIONS
from .messages import MSG_TASK_3_ANSWER
from .messages import MSG_TASK_3_OPTIONS
from .messages import MSG_TASK_4_ANSWER
from .messages import MSG_TASK_4_OPTIONS
from .messages import MSG_START_TESTING
from .messages import MSG_SKIP_TASK
from .messages import PROMPT_ERROR_START_ANSWER
from .messages import PROMPT_ERROR_INCORRECT_OPTION

from .services.user import add_user
from .services.user import get_user_by_update

from .states import STATE_START
from .states import STATE_TASK_1
from .states import STATE_TASK_2
from .states import STATE_TASK_3
from .states import STATE_TASK_4
from .states import STATE_TASK_5
from .states import STATE_FINISH

from .solutions.task_5_checker import check_task_5_solution

from .commands import init_commands
from .callbacks import init_callbacks

def serve():
    """ Start serving """
    application = ApplicationBuilder().token(environ['TELEGRAM_TOKEN']).build()

    init_commands(application)
    init_callbacks(application)

    application.run_polling()
