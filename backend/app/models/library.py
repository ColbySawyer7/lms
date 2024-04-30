from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy import Column, Integer, String

from app.db import Base

if TYPE_CHECKING:
    from app.models.user import User  # noqa: F401
    from app.models.transaction import Transaction  # noqa: F401


class Library(Base):
    __tablename__ = "libraries"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

    created: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    transactions = relationship("Transaction", back_populates="library")
