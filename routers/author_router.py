from fastapi import APIRouter
from shemas.author_shema import AddAuthor
from data_base.dal.author_dal import Author_DAL

router = APIRouter(prefix='/author', responses={404: {"description": "Not found"}})


@router.post('/add')
async def add_author(author: AddAuthor):
    dal = Author_DAL()
    await dal.add_autor(author.dict())

