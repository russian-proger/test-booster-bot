from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes

async def handle_mytest_clb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ callback handler """
    assert update.callback_query is not None
    assert update.effective_chat is not None
    assert update.effective_message is not None

    markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton('Название', callback_data='set_test_name:1'),
            InlineKeyboardButton('Настройки', callback_data='test_settings:1'),
        ],
        [
            InlineKeyboardButton('Тесты', callback_data='tests:1'),
            InlineKeyboardButton('Результаты', callback_data='results:1'),
        ],
        [
            InlineKeyboardButton('Назад к списку тестов', callback_data='mytests')
        ]
    ])

    await context.bot.edit_message_text(
        text="Настройки теста:",
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.id,
        reply_markup=markup
    )