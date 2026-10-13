
from fastapi import FastAPI, HTTPException, status, Query, Depends

from typing import Literal, Annotated
# from fastapi import  

from app.core.config import get_settings, Settings
from app.models.device import Device, DeviceCreate
from app.core.dependencies import get_device_service
from app.services.device_service import DeviceService

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

DeviceServiceDep = Annotated[
    DeviceService,
    Depends(get_device_service),
]

SettingsDep = Annotated[Settings, Depends(get_settings)]


@app.get("/health")
def health_check(settings: SettingsDep) -> dict[str, str]:
    return {
        "status": "healthy",
        "app_name": settings.app_name,
    }


@app.get("/devices", response_model=list[Device])
def read_devices(
    device_service: DeviceServiceDep,
    device_status: Literal["online", "offline"] | None = Query(
        default=None,
        alias="status",
    ),
) -> list[Device]:
    return device_service.list_devices(status=device_status)


@app.get("/devices/{device_id}", response_model=Device)
def read_device(
    device_id: int,
    device_service: DeviceServiceDep,
) -> Device:
    device = device_service.get_device(device_id)

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
def add_device(
    device_data: DeviceCreate,
    device_service: DeviceServiceDep,
) -> Device:
    return device_service.create_device(device_data)