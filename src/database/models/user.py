""" `User` table """

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from ..base import Base

class User(Base):
    """ User metadata """

    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String(60))
