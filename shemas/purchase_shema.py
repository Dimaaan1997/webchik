from pydantic import BaseModel


class AddPurchase(BaseModel):
    amount: int
    id_book: int
    id_cart: int
