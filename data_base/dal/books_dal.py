from data_base.db_config import DataBaseConnect
from data_base.db_models.book import Book
from data_base.db_models.author import Author
from sqlalchemy import insert, select


class Book_DAL:

    def __init__(self):
        self.session_fabric = DataBaseConnect()

    async def add_book(self, AddBook):
        async with self.session_fabric() as session:
            async with session.begin():
                stmt = (insert(Book).values(**AddBook))
                await session.execute(stmt)

    async def search_book_by_name(self, author):
        async with self.session_fabric() as session:
            query = await session.execute(
                select(Author.surname,
                       Book.name,
                       Book.year,
                       Book.price).join(Author).where(Book.name == book_name)
            )
            return query.all()

    async def get_book_info(self, id_book):
        async with self.session_fabric() as session:
            query = await session.execute(
                select(Author.surname,
                       Book.name,
                       Book.year,
                       Book.price).join(Author).where(Book.id_book == id_book)
            )
            return query.all()

    async def get_all_books(self):
        async with self.session_fabric() as session:
            query = await session.execute(
                select(Author.surname,
                       Book.name,
                       Book.year,
                       Book.price).join(Author)
            )
            return query.all()