
from sqlalchemy import CheckConstraint, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class DeviceDB(Base):
    __tablename__ = "devices"

    __table_args__ = (
        CheckConstraint(
            "status IN ('online', 'offline')",
            name="ck_devices_status",
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        default="offline",
    )
