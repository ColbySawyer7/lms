from fastapi import APIRouter

from app.api import items, users, utils, books, libraries, transactions

api_router = APIRouter()

api_router.include_router(utils.router, tags=["utils"])
api_router.include_router(users.router, tags=["users"])
#api_router.include_router(items.router, tags=["items"])
api_router.include_router(books.router, tags=["books"])
api_router.include_router(libraries.router, tags=["libraries"])
api_router.include_router(transactions.router, tags=["transactions"])
