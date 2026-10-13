from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.repositories.device_repository import DeviceRepository
from app.services.device_service import DeviceService


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DbSession = Annotated[Session, Depends(get_db)]


def get_device_service(db: DbSession) -> DeviceService:
    repository = DeviceRepository(db)
    return DeviceService(repository)