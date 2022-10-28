from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AddAuthor(BaseModel):
    name: str
    surname: str
    patronymic: Optional[str] = None
    birth_date: Optional[datetime] = None
