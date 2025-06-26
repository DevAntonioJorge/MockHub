from pydantic import BaseModel, EmailStr

class CreateUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class User(BaseModel):
    id: str
    username: str
    email: EmailStr
    password: str
    created_at: str 
    role: str = "user"

class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    created_at: str 
    role: str = "user"

class ListUsersResponse(BaseModel):
    users: list[UserResponse]
    length: int
    

class CreateMockServiceRequest(BaseModel):
    owner_id: str
    name: str
    route: str
    method: str
    request_schema: str | None = None
    response_payload: str
    response_code: int
    latency: int = 0

class CreateMockServiceResponse(BaseModel):
    id: str
    owner_id: str
    name: str
    route: str
    method: str
    request_schema: str | None = None
    response_payload: str
    response_code: int
    latency: int

