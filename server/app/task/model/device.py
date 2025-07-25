import socket
from enum import Enum

from pydantic import BaseModel, Field


class RegisterType(str, Enum):
    ACCOUNT = 'ACCOUNT'
    WORKER = 'WORKER'


class DeviceInfo(BaseModel):
    device_id: str = Field(default=socket.gethostname(), description='device id')
    device_name: str = Field(default=socket.gethostname(), description='device name')
    device_ip: str = Field(default=socket.gethostbyname(socket.gethostname()), description='device ip')


class RegisterModel(BaseModel):
    register_type: RegisterType = Field(..., description='Registration type')
    device_info: DeviceInfo = Field(..., description='Device information')
