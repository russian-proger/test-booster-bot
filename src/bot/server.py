""" Main File """

import time
from os import environ

from telegram import Update
from telegram.ext import ApplicationBuilder
from telegram.ext import CommandHandler
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler
from telegram.ext.filters import TEXT
from telegram.ext.filters import Document

from ..utils.constants import FOLDER_DOWNLOADS

from .messages import send_ai_message
from .messages import send_greeting
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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ `start` command handler """
    if update.effective_chat is not None and not get_user_by_update(update):
        await send_greeting(context.bot, update.effective_chat.id)
        add_user(update)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ Message handler """

    if not update.message:
        return
    
    user = get_user_by_update(update)
    if not user:
        return

    bot = context.bot
    message = update.message.text

    if user.context == STATE_START:
        if message == MSG_START_TESTING:
            user.context = STATE_TASK_1
            user.update()
            await send_task_1(bot, user.chat_id)
        else:
            await send_ai_message(bot, user.chat_id, PROMPT_ERROR_START_ANSWER, message)

    elif user.context == STATE_TASK_1:
        if message not in MSG_TASK_1_OPTIONS:
            await send_ai_message(bot, user.chat_id, PROMPT_ERROR_INCORRECT_OPTION, message)
            return

        verdict = message == MSG_TASK_1_ANSWER

        user.context = STATE_TASK_2
        user.score += int(verdict)
        user.update()


        await send_feedback(bot, user.chat_id, verdict)
        await send_task_2(bot, user.chat_id)

    elif user.context == STATE_TASK_2:
        if message not in MSG_TASK_2_OPTIONS:
            await send_ai_message(bot, user.chat_id, PROMPT_ERROR_INCORRECT_OPTION, message)
            return

        verdict = message == MSG_TASK_2_ANSWER

        user.context = STATE_TASK_3
        user.score += int(verdict)
        user.update()

        await send_feedback(bot, user.chat_id, verdict)
        await send_task_3(bot, user.chat_id)

    elif user.context == STATE_TASK_3:
        if message not in MSG_TASK_3_OPTIONS:
            await send_ai_message(bot, user.chat_id, PROMPT_ERROR_INCORRECT_OPTION, message)
            return

        verdict = message == MSG_TASK_3_ANSWER

        user.context = STATE_TASK_4
        user.score += int(verdict)
        user.update()

        await send_feedback(bot, user.chat_id, verdict)
        await send_task_4(bot, user.chat_id)

    elif user.context == STATE_TASK_4:
        if message not in MSG_TASK_4_OPTIONS:
            await send_ai_message(bot, user.chat_id, PROMPT_ERROR_INCORRECT_OPTION, message)
            return
        verdict = message == MSG_TASK_4_ANSWER

        user.context = STATE_TASK_5
        user.score += int(verdict)
        user.update()

        await send_feedback(bot, user.chat_id, verdict)
        await send_task_5(bot, user.chat_id)

    elif user.context == STATE_TASK_5:
        if message == MSG_SKIP_TASK:
            return

        if not update.message.document:
            return

        filename = f"task_5_{user.id}_{time.time()}.py"
        f = await bot.get_file(update.message.document)

        filepath = FOLDER_DOWNLOADS / filename
        await f.download_to_drive(filepath)

        result = check_task_5_solution(filepath)
        verdict = (result[0] == result[1])

        user.context = STATE_FINISH
        user.score += int(verdict)
        user.update()

        await send_feedback(bot, user.chat_id, verdict)
        await send_finish(bot, user.chat_id, [user.score, 5])

    elif user.context == STATE_FINISH:
        pass

    else:
        user.context = STATE_START
        user.update()

def serve():
    """ Start serving """
    application = ApplicationBuilder().token(environ['TELEGRAM_TOKEN']).build()

    start_handler = CommandHandler('start', start)

    application.add_handler(start_handler)
    application.add_handler(MessageHandler(TEXT, handle_message))
    application.add_handler(MessageHandler(Document.ALL, handle_message))

    application.run_polling()
