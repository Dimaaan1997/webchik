import sqlalchemy
from data_base.db_config import DataBaseConnect
from data_base.db_models.cart import Cart
from data_base.db_models.author import Author
from data_base.db_models.book import Book
from data_base.db_models.purchase import Purchase
from data_base.db_config import DataBaseConnect
from sqlalchemy import insert, select
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

    async def get_cart_by_id(self, id_cart):
        async with self.session_fabric() as session:
            stmt = (select(Author.surname, Book.name, Book.year, Purchase.amount, Book.price).
                    join(Book, Purchase.id_book == Book.id_book).
                    join(Author, Book.id_author == Author.id_author).where(Purchase.id_cart == id_cart))
            result = await session.execute(stmt)
            return result.all()