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


def get_device(device_id: int) -> Device | None:
    """Return a device by ID, or None if it doesn't exist."""
    return DEVICES.get(device_id)

def list_devices() -> list[Device]:
    return list(DEVICES.values())

def create_device(device_data: DeviceCreate) -> Device:
    next_id = max(DEVICES, default = 0) + 1

    device = Device(
        id = next_id,
        name= device_data.name,
        status= device_data.status
    )

    DEVICES[next_id]=device
    return device