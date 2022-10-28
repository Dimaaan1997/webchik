from sqlalchemy import ( Column,Integer, DATE, ForeignKey)
from data_base.db_config import Base


class Cart(Base):
    __tablename__ = 'cart'

    id_cart = Column(Integer, primary_key=True)

    date = Column(DATE, nullable=True)
    cost = Column(Integer, nullable= True)

    id_client = Column(Integer, ForeignKey('client.id_client', ondelete='CASCADE'))