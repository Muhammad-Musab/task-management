# app/schemas.py

from pydantic import BaseModel
from datetime import datetime

# Schema for task creation request
class TaskCreate(BaseModel):
    title: str
    short_description: str  # Short description for the task
    description: str

    class Config:
        orm_mode = True

# Task response schema
class TaskBase(BaseModel):
    id: int
    title: str
    short_description: str
    description: str
    created_at: datetime  # To include created time

    class Config:
        orm_mode = True

# Task response schema for returning task to user
class Task(TaskBase):
    class Config:
        orm_mode = True
