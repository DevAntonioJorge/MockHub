from pydantic import BaseModel, EmailStr
from uuid import UUID

class CreateUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class CreateUserResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr

class CreateMockServiceRequest(BaseModel):
    owner_id: UUID
    name: str
    route: str
    method: str
    request_schema: str | None = None
    response_payload: str
    response_code: int
    latency: int = 0

class CreateMockServiceResponse(BaseModel):
    id: UUID
    owner_id: UUID
    name: str
    route: str
    method: str
    request_schema: str | None = None
    response_payload: str
    response_code: int
    latency: int

