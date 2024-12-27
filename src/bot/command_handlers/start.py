""" `/start` command handler """

from telegram import BotCommand
from telegram import BotCommandScopeChat
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from ..views.greeting import generate_greeting_msg
from ..services.user import add_user
from ..services.user import get_user_by_update

async def handle_start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ `start` command handler """
    assert update.message is not None
    if update.effective_chat is None: return

    # Check for user existance in database
    if get_user_by_update(update) is None:
        add_user(update)

    bot = context.bot
    chat_id = update.effective_chat.id

    # Set new commands
    await bot.set_my_commands(commands = [
            BotCommand('newtest', 'Создать новый тест'),
            BotCommand('mytests', 'Список созданных тестов')
        ],
        scope=BotCommandScopeChat(chat_id)
    )

    # Send message
    message = generate_greeting_msg(name=update.message.chat.first_name)
    await bot.send_message(
        chat_id=chat_id,
        text=message.text,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=message.markup
    )
