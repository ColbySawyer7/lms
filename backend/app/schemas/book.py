from pydantic import BaseModel
from datetime import date

class BookCreate(BaseModel):
    title: str
    author: str
    isbn: str
    publication_date: date
    genre: str


class BookUpdate(BookCreate):
    pass


class Book(BookCreate):
    id: int

    class Config:
        orm_mode = True
