from typing import Any, List
from fastapi import APIRouter, HTTPException
from sqlalchemy import select, func
from starlette.responses import Response

from app.deps.db import CurrentAsyncSession
from app.deps.request_params import BookRequestParams
from app.models.book import Book
from app.models.library import Library
from app.schemas.book import Book as BookSchema, BookCreate, BookUpdate

router = APIRouter(prefix="/books")

@router.get("", response_model=List[BookSchema])
async def get_books(response: Response, session: CurrentAsyncSession, request_params: BookRequestParams) -> Any:
    total = await session.scalar(
        select(func.count(Book.id))
    )
    books = (await session.execute(select(Book))).scalars().all()
    response.headers[
        "Content-Range"
    ] = f"{request_params.skip}-{request_params.skip + len(books)}/{total}"
    return books

@router.post("", response_model=BookSchema, status_code=201)
async def create_book(book_in: BookCreate, session: CurrentAsyncSession) -> Any:
    book = Book(**book_in.dict())
    session.add(book)
    await session.commit()
    return book

@router.put("/{book_id}", response_model=BookSchema)
async def update_book(book_id: int, book_in: BookUpdate, session: CurrentAsyncSession) -> Any:
    book: Book = await session.get(Book, book_id)
    if not book:
        raise HTTPException(404)
    update_data = book_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(book, field, value)
    session.add(book)
    await session.commit()
    return book


@router.get("/{book_id}", response_model=BookSchema)
async def get_book(book_id: int, session: CurrentAsyncSession) -> Any:
    book: Book = await session.get(Book, book_id)
    if not book:
        raise HTTPException(404)
    return book

@router.delete("/{book_id}")
async def delete_book(book_id: int, session: CurrentAsyncSession) -> Any:
    book: Book = await session.get(Book, book_id)
    if not book:
        raise HTTPException(404)
    session.delete(book)
    await session.commit()
    return {"success": True}
