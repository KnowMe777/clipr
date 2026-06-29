from sqlalchemy import (
    BigInteger,
    DateTime,
    Index,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Click(Base):
    __tablename__ = "clicks"

    __table_args__ = (
        Index("idx_clicks_short_code", "short_code",),
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

    clicked_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )