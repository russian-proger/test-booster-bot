""" Main File """

from os import environ

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from ..gigachat.generator import generate_start_message

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ `start` command handler """

    if update.effective_chat is not None:
        message = generate_start_message()
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def serve():
    """ Start serving """
    application = ApplicationBuilder().token(environ['TELEGRAM_TOKEN']).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()
