from data_base.db_models.purchase import Purchase
from data_base.db_config import DataBaseConnect
from sqlalchemy import insert


class Purchase_DAL:

    def __init__(self):
        self.session_fabric = DataBaseConnect()

    async def add_purchase(self, AddPurchase: dict):
        async with self.session_fabric() as session:
            async with session.begin():
                stmt = (insert(Purchase).values(**AddPurchase))
                await session.execute(stmt)