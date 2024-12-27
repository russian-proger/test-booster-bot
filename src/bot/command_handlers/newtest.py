from telegram import Update
from telegram.ext import ContextTypes

from ..context import CTX_NEW_TEST
from ..services.user import get_user_by_update

async def handle_newtest_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ `newtest` command handler """
    
    # Ignore this message
    if update.effective_chat is None: return

    user = get_user_by_update(update)
    assert user is not None

    user.context = CTX_NEW_TEST
    user.update()

    await context.bot.send_message(
        update.effective_chat.id,
        'Введите название нового теста:',
    )
