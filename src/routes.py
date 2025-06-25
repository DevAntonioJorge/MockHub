from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from .db import get_session
from sqlmodel import Session, select
from .models import User

user_router = APIRouter(prefix="/users", tags=["users"])
mock_service_router = APIRouter(prefix="/mock-services", tags=["mock_services"])
request_log_router = APIRouter(prefix="/request-logs", tags=["request_logs"])

@user_router.get("/")
def read_users(db: Session = Depends(get_session)) -> JSONResponse:
    stmt = select(User).where()
    result = db.exec(stmt).all()
    return JSONResponse(content=[user for user in result])

    