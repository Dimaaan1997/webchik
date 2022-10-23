from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DATE,
    ForeignKey
)
from sqlalchemy.orm import relationship
from data_base.db_config import Base


class Book(Base):
    __tablename__ = 'book'

    id_book = Column(Integer, primary_key=True)

    name = Column(String(32), nullable=True)
    year = Column(Integer, nullable=True)
    price = Column(Integer, nullable=True)

    id_author = Column(Integer, ForeignKey('author.id_author', ondelete='CASCADE'))
