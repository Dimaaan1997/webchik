from data_base.db_models.client import Client
from data_base.db_config import DataBaseConnect
from sqlalchemy import insert, select


class Client_DAL:

    def __init__(self):
        self.session_fabric = DataBaseConnect()

    async def add_client(self, AddClient:dict):
        async with self.session_fabric() as session:
            async with session.begin():
                stmt = (insert(Client).values(**AddClient))
                await session.execute(stmt)

    async def search_client(self, name:str, number:str):
        async with self.session_fabric() as session:
            query = await session.execute(
                select(Client.name,
                       Client.phone_number,
                       Client.address).where(Client.name == name, Client.phone_number == number))
            return query.all()
