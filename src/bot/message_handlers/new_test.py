from telegram import Update
from telegram.ext import ContextTypes

from ..context import CTX_NEW_TEST
from ..helper import handle_context

@handle_context(CTX_NEW_TEST)
async def handle_new_test_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    assert update.effective_chat
    await context.bot.send_message(update.effective_chat.id, 'переделывай')
