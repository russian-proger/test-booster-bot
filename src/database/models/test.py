""" `Test` table """

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from ..base import Base

class Test(Base):
    """ Test metadata """

    __tablename__ = "test"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60))
