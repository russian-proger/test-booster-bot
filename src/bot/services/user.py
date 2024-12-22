""" Services for `start` command """

from telegram import Update

from ...database.engine import create_session
from ...database.models.user import User

from ..states import *

def get_user_by_update(update: Update) -> User | None:
    """ Find user by updating information """
    if not update.message or not update.message.from_user:
        return None
    return User.find_by_chat_id(update.message.from_user.id)

def add_user(update: Update):
    """ Add user to the DB """
    if not update.message or not update.message.from_user:
        return

    with create_session() as session:
        user_info = update.message.from_user

        if get_user_by_update(update):
            return

        user = User(
            fullname=f"{user_info.first_name} {user_info.last_name}",
            username=user_info.username,
            chat_id=user_info.id,
            context=STATE_START
        )

        session.add(user)
        session.commit()
