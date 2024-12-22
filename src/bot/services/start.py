""" Services for `start` command """

from telegram import Update

from ...database.engine import create_session
from ...database.models.user import User

def add_user(update: Update):
    """ Add user to the DB """
    if not update.message or not update.message.from_user:
        return

    with create_session() as session:
        user_info = update.message.from_user

        if User.find_by_chat_id(user_info.id):
            return

        user = User(
            fullname=f"{user_info.first_name} {user_info.last_name}",
            username=user_info.username,
            chat_id=user_info.id,
            context="start"
        )

        session.add(user)
        session.commit()
