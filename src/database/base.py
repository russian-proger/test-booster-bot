""" Base class """

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm.attributes import InstrumentedAttribute


from .engine import create_session

class Base(DeclarativeBase):
    """ Base class """

    id: Mapped[int] = mapped_column(primary_key=True)

    def update(self):
        """ Flush changes """
        with create_session() as session:
            mapped_values = {}
            for item in dir(self.__class__):
                field_name = item
                field_type = type(self.__class__.__dict__.get(item, None))
                is_column = field_type is InstrumentedAttribute

                if is_column:
                    mapped_values[field_name] = getattr(self, field_name)

            session.query(self.__class__).filter(self.__class__.id == self.id).update(mapped_values)
            session.commit()
