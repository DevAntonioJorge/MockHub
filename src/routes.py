from fastapi import APIRouter, Depends, HTTPException
from .db import get_session
from sqlmodel import Session, select
from .models import User
from .schemas import CreateUserRequest, ListUsersResponse, UserResponse
from .utils import hash_password


user_router = APIRouter(prefix="/users", tags=["users"])
mock_service_router = APIRouter(prefix="/mock-services", tags=["mock_services"])
request_log_router = APIRouter(prefix="/request-logs", tags=["request_logs"])

@user_router.get("/", response_model=ListUsersResponse)
def read_users(db: Session = Depends(get_session)):
    stmt = select(User).where()
    result = db.exec(stmt).all()
    users = [UserResponse(id=str(user.id), username=user.username, email=user.email, created_at=str(user.created_at)) for user in result]
    return ListUsersResponse(users=users, length=len(users))

@user_router.post("/")
def create_user(request: CreateUserRequest, db: Session = Depends(get_session)) :
    user = User(
        username=request.username,
        email=request.email,
        password=hash_password(request.password), 
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created successfully"}

@user_router.get("/{user_id}")
def read_user(user_id: str, db: Session = Depends(get_session)):
    stmt = select(User).where(User.id == user_id)
    user = db.exec(stmt).first()
    if not user:
        return HTTPException(status_code=404, detail={"message": "User not found"})
    
    return UserResponse(
        id=str(user.id),
        username=user.username,
        email=user.email,
        created_at=str(user.created_at),
        role=user.role
    )

    