from fastapi import APIRouter, FastAPI, Depends
from helpers import get_settings, Settings
router = APIRouter(
    prefix="/api",
    tags=["base"]
)

@router.get('/')
def welcome(app_settings: Settings = Depends(get_settings)):
    
    app_name = app_settings.APP_NAME
    app_ver = app_settings.APP_VERSION
    return {"message": f"Welcome to {app_name} version {app_ver}"}