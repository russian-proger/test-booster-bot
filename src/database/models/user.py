""" `User` table """

from typing import Optional
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from ..base import Base
from ..engine import create_session

class User(Base):
    """ User metadata """
    __tablename__ = "user"

    chat_id: Mapped[int] = mapped_column(Integer(), unique=True)
    fullname: Mapped[str] = mapped_column(String(60))
    username: Mapped[str] = mapped_column(String(60))
    context: Mapped[str] = mapped_column(String(60))

    @staticmethod
    def find_by_chat_id(chat_id: int) -> 'User|None':
        """ Return User by chat_id """
        with create_session() as session:
            return session.query(User).where(User.chat_id == chat_id).one_or_none()
