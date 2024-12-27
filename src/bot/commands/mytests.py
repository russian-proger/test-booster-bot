from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes

async def handle_mytests_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ `newtest` command handler """
    
    # Ignore this message
    if update.effective_chat is None: return

    markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton('Логистическая регрессия', callback_data='mytest:1'),
            InlineKeyboardButton('Наивный байес', callback_data='mytest:2'),
        ],
        [
            InlineKeyboardButton('K-means', callback_data='mytest:3'),
            InlineKeyboardButton('Ансамбли', callback_data='mytest:4'),
        ],
    ])

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Выберите тест из списка:",
        reply_markup=markup
    )