from pydantic import BaseModel, UUID4
from datetime import date

class TransactionCreate(BaseModel):
    book_id: int
    user_id: UUID4
    library_id: int


class TransactionUpdate(TransactionCreate):
    status: str
    return_date: date
    pass


class Transaction(TransactionCreate):
    id: int

    class Config:
        orm_mode = True
