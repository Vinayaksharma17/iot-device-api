
from fastapi import FastAPI, HTTPException, status

from app.core.config import get_settings
from app.models.device import Device, DeviceCreate
from app.services.device_service import (
    create_device,
    get_device,
    list_devices,
)

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/devices", response_model=list[Device])
def read_devices() -> list[Device]:
    return list_devices()


@app.get("/devices/{device_id}", response_model=Device)
def read_device(device_id: int) -> Device:
    device = get_device(device_id)

    if device is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Device {device_id} not found",
        )

    return device


@app.post(
    "/devices",
    response_model=Device,
    status_code=status.HTTP_201_CREATED,
)
def add_device(device_data: DeviceCreate) -> Device:
    return create_device(device_data)
