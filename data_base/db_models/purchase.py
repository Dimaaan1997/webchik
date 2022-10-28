from sqlalchemy import ( Column, Integer, ForeignKey)
from data_base.db_config import Base


class Purchase(Base):
    __tablename__ = 'purchase'

    id_purchase = Column(Integer, primary_key=True)

    amount = Column(Integer, nullable=True)
    id_book = Column(Integer, ForeignKey('book.id_book', ondelete='CASCADE'))
    id_cart = Column(Integer, ForeignKey('cart.id_cart', ondelete='CASCADE'))