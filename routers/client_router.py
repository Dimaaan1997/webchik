from fastapi import APIRouter
from shemas.client_shema import AddClient, SearchClient
from data_base.dal.client_dal import Client_DAL
from fastapi import HTTPException, status

client_router = APIRouter(prefix='/client', responses={404: {"description": "Not found"}})


@client_router.post('/new')
async def add_client(client: AddClient):
    dal = Client_DAL()
    await dal.add_client(client.dict())


@client_router.get('/search')
async def search_client(client: SearchClient):
    dal = Client_DAL()
    client = await dal.search_client(client.name, client.phone_number)
    if client:
        return client
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)