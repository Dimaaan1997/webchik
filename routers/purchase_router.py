from fastapi import APIRouter
from shemas.purchase_shema import AddPurchase
from data_base.dal.purchase_dal import Purchase_DAL

purchase_router = APIRouter(prefix='/purchase', responses={404: {"description": "Not found"}})


@purchase_router.post('/add')
async def add_purchase(purchase: AddPurchase):
    dal = Purchase_DAL()
    await dal.add_purchase(purchase.dict())
