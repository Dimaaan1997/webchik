from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
)
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

load_dotenv()
type_DB = os.getenv('TYPE_BD')
user = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
host = os.getenv('HOST_PORT')
name_DB = os.getenv('NAME_DB')
connect_route = f'{type_DB}://{user}:{password}@{host}/{name_DB}'


class DataBaseConnect:
    __instance__ = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance__:
            engine = create_async_engine(connect_route, future=True,
                                         echo=False)
            async_session_fabric = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
            cls.__instance__ = async_session_fabric

        return cls.__instance__
