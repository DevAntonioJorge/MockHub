from fastapi import APIRouter

user_router = APIRouter(prefix="/users", tags=["users"])
mock_service_router = APIRouter(prefix="/mock-services", tags=["mock_services"])
request_log_router = APIRouter(prefix="/request-logs", tags=["request_logs"])

