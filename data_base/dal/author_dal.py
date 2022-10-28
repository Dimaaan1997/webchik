from data_base.db_config import DataBaseConnect
from data_base.db_models.author import Author
from sqlalchemy import insert


class Author_DAL:

    def __init__(self):
        self.session_fabric = DataBaseConnect()

    async def add_autor(self, AddAuthor):
        async with self.session_fabric() as session:
            async with session.begin():
                stmt = (insert(Author).values(**AddAuthor))
                await session.execute(stmt)


