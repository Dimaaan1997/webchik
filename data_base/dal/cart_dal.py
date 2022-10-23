import sqlalchemy
from data_base.db_config import DataBaseConnect
from data_base.db_models.cart import Cart
from data_base.db_config import DataBaseConnect
import asyncio
from sqlalchemy import insert
from datetime import datetime


class Cart_DAL:

    def __init__(self):
        self.session_fabric = DataBaseConnect()

    async def add_cart(self, id_client):
        async with self.session_fabric() as session:
            async with session.begin():
                stmt = (insert(Cart).values(date=datetime.now().date(),
                                            id_client=id_client))
                await session.execute(stmt)

