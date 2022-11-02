from fastapi import APIRouter
from data_base.dal.cart_dal import Cart_DAL
from shemas.cart_shema import SearchCart
from fastapi import HTTPException, status

cart_router = APIRouter(prefix='/cart', responses={404: {"description": "Not found"}})


@cart_router.post('/add_cart_to/{id_client}')
async def add_cart(id_client: int):
    dal = Cart_DAL()
    await dal.add_cart(id_client=id_client)


@cart_router.post('/add')
async def get_cart(id_cart: SearchCart):
    dal = Cart_DAL()
    cart = await dal.get_cart_by_id(id_cart.id)
    if cart:
        return cart
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)