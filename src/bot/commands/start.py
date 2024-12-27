""" `/start` command handler """

from telegram import BotCommand
from telegram import BotCommandScopeChat
from telegram import ReplyKeyboardRemove
from telegram import Update
from telegram.ext import ContextTypes

from ..services.user import add_user
from ..services.user import get_user_by_update

async def handle_start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ `start` command handler """
    if update.effective_chat is None: return

    user = get_user_by_update(update)
    if user is not None: return

    add_user(update)

    markup = ReplyKeyboardRemove()
    commands = [
        BotCommand('newtest', 'Создать новый тест'),
        BotCommand('mytests', 'Список созданных тестов')
    ]

    bot = context.bot
    chat_id = update.effective_chat.id

    await bot.set_my_commands(commands, scope=BotCommandScopeChat(chat_id))
    await bot.send_message(
        chat_id=chat_id,
        text=greeting_message,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )