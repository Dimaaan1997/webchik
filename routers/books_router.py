from fastapi import APIRouter
from shemas.book_shema import SearchBook, AddBook
from data_base.dal.books_dal import Book_DAL

router = APIRouter(prefix='/book', responses={404: {"description": "Not found"}})


@router.post('/add')
async def add_book(book: AddBook):
    dal = Book_DAL()
    await dal.add_book(book.dict())


async def