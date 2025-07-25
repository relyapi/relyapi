from enum import Enum

from pydantic import BaseModel, Field


class TaskType(str, Enum):
    LOGIN = 'login'
    REGISTER = 'register'
    ALIVE = 'alive'


class TaskInfo(BaseModel):
    pass


class RegisterModel(BaseModel):
    task_type: TaskType = Field(..., description='task type')
    task_info: TaskInfo = Field(..., description='task info')
