from sqlalchemy import (Column, Integer, String)
from sqlalchemy.orm import relationship
from data_base.db_config import Base
from data_base.db_models.cart import Cart


class Client(Base):
    __tablename__ = 'client'

    id_client = Column(Integer, primary_key=True)

    name = Column(String(32), nullable=True)
    phone_number = Column(String(32), nullable=True)
    address = Column(String(256), nullable= True)

    client = relationship(Cart, cascade="all, delete", backref="client")