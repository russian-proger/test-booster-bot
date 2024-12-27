""" `User` table """

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .engine import create_session

class User(Base):
    """ User metadata """
    __tablename__ = "user"

    chat_id: Mapped[int] = mapped_column(Integer(), unique=True)
    firstname: Mapped[str] = mapped_column(String(60))
    lastname: Mapped[str] = mapped_column(String(60))
    fullname: Mapped[str] = mapped_column(String(60))
    username: Mapped[str] = mapped_column(String(60))
    context: Mapped[str] = mapped_column(String(60))
    score: Mapped[int] = mapped_column(Integer(), default=0)
    f_tests: Mapped[List['Test']] = relationship(back_populates='f_author')

    @staticmethod
    def find_by_chat_id(chat_id: int) -> 'User|None':
        """ Return User by chat_id """
        with create_session() as session:
            return session.query(User).where(User.chat_id == chat_id).one_or_none()

class Test(Base):
    """ Test metadata """
    __tablename__ = "test"

    name: Mapped[str] = mapped_column(String(60))
    context: Mapped[str] = mapped_column(String(60))
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    f_author: Mapped['User'] = relationship(back_populates='f_tests')
