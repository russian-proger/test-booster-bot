from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes

async def handle_newtest_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ `newtest` command handler """
    
    # Ignore this message
    if update.effective_chat is None: return

    
