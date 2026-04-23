from fastapi import APIRouter, FastAPI
import os

router = APIRouter(
    prefix="/api",
    tags=["base"]
)

@router.get('/')
def welcome():
    app_name = os.getenv("APP_NAME")
    app_ver = os.getenv("APP_VERSION")
    return {"message": f"Welcome to {app_name} version {app_ver}"}