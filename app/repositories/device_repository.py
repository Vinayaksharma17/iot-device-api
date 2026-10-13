from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.device_db import DeviceDB


class DeviceRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(self, device_id: int) -> DeviceDB | None:
        return self.db.get(DeviceDB, device_id)

    def list_devices(
        self,
        status: str | None = None,
    ) -> list[DeviceDB]:
        statement = select(DeviceDB)

        if status is not None:
            statement = statement.where(DeviceDB.status == status)

        return list(self.db.scalars(statement).all())

    def create(
        self,
        name: str,
        status: str,
    ) -> DeviceDB:
        device = DeviceDB(name=name, status=status)
        self.db.add(device)
        self.db.commit()
        self.db.refresh(device)
        return device