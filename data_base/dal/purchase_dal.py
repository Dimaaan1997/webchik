from data_base.db_models.purchase import Purchase
from data_base.db_config import DataBaseConnect
from sqlalchemy import insert, select
import asyncio

# amount = Column(Integer, nullable=True)
# id_book = Column(Integer, ForeignKey('book.id_book', ondelete='CASCADE'))
# id_cart = Column(Integer, ForeignKey('cart.id_cart', ondelete='CASCADE'))

test_purchase = {'amount': 1, 'id_book': 3, 'id_cart': 1}

class Purchase_DAL:

    def __init__(self):
        self.session_fabric = DataBaseConnect()

    async def add_purchase(self, AddPurchase: dict):
        async with self.session_fabric() as session:
            async with session.begin():
                stmt = (insert(Purchase).values(**AddPurchase))
                await session.execute(stmt)



a = Purchase_DAL()
asyncio.run(a.add_purchase(test_purchase))