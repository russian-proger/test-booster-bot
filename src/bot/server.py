""" Main File """

from os import environ

from telegram import Update
from telegram.ext import ApplicationBuilder
from telegram.ext import CommandHandler
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler
from telegram.ext.filters import TEXT

from .messages import send_greeting
from .messages import send_ai_message
from .messages import MSG_START_TESTING
from .messages import PROMPT_ERROR_START_ANSWER

from .states import STATE_START
from .states import STATE_TASK_1
from .services.user import add_user
from .services.user import get_user_by_update

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ `start` command handler """
    if update.effective_chat is not None:
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
        else:
            await send_ai_message(bot, user.chat_id, PROMPT_ERROR_START_ANSWER, message)




def serve():
    """ Start serving """
    application = ApplicationBuilder().token(environ['TELEGRAM_TOKEN']).build()

    start_handler = CommandHandler('start', start)

    application.add_handler(start_handler)
    application.add_handler(MessageHandler(TEXT, handle_message))

    application.run_polling()
