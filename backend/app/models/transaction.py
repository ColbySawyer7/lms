from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.sql import text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import expression

from app.db import Base


if TYPE_CHECKING:
    from app.models.user import User  # noqa: F401
    from app.models.book import Book  # noqa: F401
    from app.models.library import Library  # noqa: F401


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    library_id = Column(Integer, ForeignKey('libraries.id'))
    #checkout_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    #due_date = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP + INTERVAL '14 days'"), nullable=True)
    #return_date = Column(Date, nullable=True)
    status = Column(String)

    created: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    book = relationship("Book", back_populates="transactions")
    user = relationship("User", back_populates="transactions")
    library = relationship("Library", back_populates="transactions")
