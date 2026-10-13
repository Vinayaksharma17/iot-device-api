from app.models.device import Device, DeviceCreate
from app.repositories.device_repository import DeviceRepository


class DeviceService:
    def __init__(self, repository: DeviceRepository) -> None:
        self.repository = repository

    def get_device(self, device_id: int) -> Device | None:
        record = self.repository.get_by_id(device_id)

        if record is None:
            return None

        return Device(
            id=record.id,
            name=record.name,
            status=record.status,
        )

    def list_devices(
        self,
        status: str | None = None,
    ) -> list[Device]:
        records = self.repository.list_devices(status=status)

        return [
            Device(
                id=record.id,
                name=record.name,
                status=record.status,
            )
            for record in records
        ]

    def create_device(self, data: DeviceCreate) -> Device:
        record = self.repository.create(
            name=data.name,
            status=data.status,
        )

        return Device(
            id=record.id,
            name=record.name,
            status=record.status,
        )