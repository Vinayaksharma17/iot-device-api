from typing import Literal

from pydantic import BaseModel, Field

DeviceStatus = Literal["online", "offline"]

class DeviceCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    status: DeviceStatus = "offline"


class Device(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=3, max_length=50)
    status: Literal["online", "offline"]