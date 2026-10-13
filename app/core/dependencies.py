from app.services.device_service import DeviceService

def get_device_service() -> DeviceService:
    return DeviceService()