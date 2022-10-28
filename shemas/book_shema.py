from pydantic import BaseModel
from pydantic import conint, constr
from typing import Optional


class SearchBook(BaseModel):
    name: constr(max_length=32)


class AddBook(SearchBook):
    name: constr(max_length=32)
    year: Optional[conint(strict=True, ge=1)] = None
    price: conint(strict=True, ge=1)
    id_author: int
