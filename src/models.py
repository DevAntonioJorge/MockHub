from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime
from uuid import uuid4, UUID

class User(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    username: str = Field(index=True, unique=True, max_length=50)
    email: str = Field(index=True, unique=True, max_length=100)
    password: str = Field(max_length=100)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    role: str = Field(default="user", max_length=20)

class MockService(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    owner_id: UUID = Field(foreign_key="user.id", nullable=False)
    name: str = Field(index=True, unique=True, max_length=100)
    route: str = Field(index=True, max_length=100)
    method: str = Field(index=True, max_length=10)
    request_schema: Optional[str] = Field(default=None, max_length=500)
    response_payload: str = Field(max_length=500)
    response_code: int
    latency: int = Field(default=0)
    

class RequestLog(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    service_id: UUID = Field(foreign_key="mockservice.id")
    timestamp: datetime = Field(default_factory=datetime.now)
    request_payload: str
    response_payload: str
    status_code: int
    latency_ms: int