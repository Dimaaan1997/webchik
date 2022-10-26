from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DATE
)
from sqlalchemy.orm import relationship
from data_base.db_config import Base
from data_base.db_models.book import Book


class Author(Base):
    __tablename__ = 'author'

    id_author = Column(Integer, primary_key=True)

    name = Column(String(32), nullable=True)
    surname = Column(String(32), nullable=True)
    patronymic = Column(String(32), nullable=True)
    birth_date = Column(DATE, nullable=True)

    author = relationship(Book,  backref='author', cascade="all, delete")
