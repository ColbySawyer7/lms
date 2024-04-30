from typing import Any, List
from fastapi import APIRouter, HTTPException
from sqlalchemy import select, func
from starlette.responses import Response

from app.deps.db import CurrentAsyncSession
from app.models.transaction import Transaction
from app.schemas.transaction import Transaction as TransactionSchema, TransactionCreate, TransactionUpdate
from app.deps.request_params import TrasnactionRequestParams

router = APIRouter(prefix="/transactions")

@router.get("/count")
async def count_transactions(response: Response, session: CurrentAsyncSession) -> Any:
    result = await session.execute(select(func.count(Transaction.id)))
    count = result.scalar_one()
    return count

@router.get("", response_model=List[TransactionSchema])
async def get_transactions(response: Response, session: CurrentAsyncSession, request_params: TrasnactionRequestParams) -> Any:
    total = await session.scalar(
        select(func.count(Transaction.id))
    )
    transactions = (
        (
            await session.execute(
                select(Transaction)
                .offset(request_params.skip)
                .limit(request_params.limit)
                .order_by(request_params.order_by)
            )
        )
        .scalars()
        .all()
    )
    response.headers[
        "Content-Range"
    ] = f"{request_params.skip}-{request_params.skip + len(transactions)}/{total}"
    return transactions

@router.post("", response_model=TransactionSchema, status_code=201)
async def create_transaction(transaction_in: TransactionCreate, session: CurrentAsyncSession) -> Any:
    transaction = Transaction(**transaction_in.dict())
    session.add(transaction)
    await session.commit()
    return transaction

@router.put("/{transaction_id}", response_model=TransactionSchema)
async def update_transaction(transaction_id: int, transaction_in: TransactionUpdate, session: CurrentAsyncSession) -> Any:
    transaction: Transaction = await session.get(Transaction, transaction_id)
    if not transaction:
        raise HTTPException(404)
    update_data = transaction_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(transaction, field, value)
    session.add(transaction)
    await session.commit()
    return transaction

@router.get("/{transaction_id}", response_model=TransactionSchema)
async def get_transaction(transaction_id: int, session: CurrentAsyncSession) -> Any:
    transaction: Transaction = await session.get(Transaction, transaction_id)
    if not transaction:
        raise HTTPException(404)
    return transaction

@router.delete("/{transaction_id}")
async def delete_transaction(transaction_id: int, session: CurrentAsyncSession) -> Any:
    transaction: Transaction = await session.get(Transaction, transaction_id)
    if not transaction:
        raise HTTPException(404)
    await session.commit()
    return transaction
