from app.models.device import Device, DeviceCreate

DEVICES: dict[int, Device] = {
    1: Device(
        id=1,
        name="Temperature Sensor 01",
        status="online",
    ),
    2: Device(
        id=2,
        name="Humidity Sensor 01",
        status="offline",
    ),
}



class DeviceService:
    def get_device(self, device_id: int) -> Device | None:
        return DEVICES.get(device_id)

    def list_devices(
        self,
        status: str | None = None,
    ) -> list[Device]:
        devices = list(DEVICES.values())

        if status is None:
            return devices

        return [
            device for device in devices
            if device.status == status
        ]

    def create_device(self, data: DeviceCreate) -> Device:
        next_id = max(DEVICES, default=0) + 1

        device = Device(
            id=next_id,
            name=data.name,
            status=data.status,
        )
        DEVICES[next_id] = device
        return device
