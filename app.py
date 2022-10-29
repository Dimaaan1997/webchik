from fastapi import FastAPI
from routers.client_router import client_router
from routers.cart_router import cart_router
from routers.author_router import author_router
from routers.purchase_router import purchase_router
from routers.books_router import book_router
from routers.auth_router import auth_router


app = FastAPI(root_path='/web/course')

app.include_router(client_router)
app.include_router(cart_router)
app.include_router(author_router)
app.include_router(purchase_router)
app.include_router(book_router)
app.include_router(auth_router)