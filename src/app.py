from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .db import create_db_and_tables, get_session
from .routes import user_router, mock_service_router, request_log_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan, dependencies=[Depends(get_session)])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],          
    allow_headers=["*"],  
)

app.include_router(user_router)
app.include_router(mock_service_router)
app.include_router(request_log_router)