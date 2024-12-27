from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes

async def handle_list_my_tests_clb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ `mytest` callback query handler """
    assert update.callback_query is not None
    assert update.effective_chat is not None
    assert update.effective_message is not None

    markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton('Логистическая регрессия', callback_data='mytest:1'),
            InlineKeyboardButton('Наивный байес', callback_data='mytest:1'),
        ],
        [
            InlineKeyboardButton('K-means', callback_data='mytest:1'),
            InlineKeyboardButton('Ансамбли', callback_data='mytest:1'),
        ],
    ])

    await context.bot.edit_message_text(
        text="Выберите тест из списка:",
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.id,
        reply_markup=markup
    )
