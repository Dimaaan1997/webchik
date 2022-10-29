from fastapi import APIRouter


auth_router = APIRouter(prefix="/auth",responses={404: {"description": "Not found"}})