from fastapi import APIRouter
from shemas.book_shema import SearchBook, AddBook
from data_base.dal.books_dal import Book_DAL
from fastapi import HTTPException, status

book_router = APIRouter(prefix='/book', responses={404: {"description": "Not found"}})


@book_router.post('/add')
async def add_book(book: AddBook):
    dal = Book_DAL()
    await dal.add_book(book.dict())


@book_router.get('/search')
async def search_book(name: SearchBook):
    dal = Book_DAL()
    book = await dal.search_book_by_name(name.name)
    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@book_router.get('/get')
async def get_book(id_book: int):
    dal = Book_DAL()
    book = await dal.get_book_info(id_book)
    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@book_router.get('/all')
async def get_book():
    dal = Book_DAL()
    books = await dal.get_all_books()
    if books:
        return books
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

