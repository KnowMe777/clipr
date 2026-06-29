from sqlalchemy import (
    BigInteger,
    Boolean,
    DateTime,
    Index,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Url(Base):
    __tablename__ = "urls"

    __table_args__ = (
        Index("idx_urls_short_code", "short_code", unique=True),
        Index("idx_urls_expires_at", "expires_at"),
    )

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    short_code: Mapped[str] = mapped_column(
        String(16),
        nullable=False,
    )

    original_url: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    expires_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    is_custom: Mapped[bool] = mapped_column(
        Boolean,
        server_default="false",
        nullable=False,
    )