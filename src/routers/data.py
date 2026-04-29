import os
import logging
from fastapi.responses import JSONResponse
from models import ResponseEnum
from fastapi import APIRouter, FastAPI, Depends, UploadFile, status
from helpers import get_settings, Settings
from controllers import DataController
from controllers import ProjectController
import aiofiles

logger =  logging.getLogger("uvicorn_error")

data_router = APIRouter(
    prefix="/api/data",
    tags=["data"]
)

@data_router.post('/upload/{project_id}')
async def upload_data(project_id:str, file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):
    controller = DataController()
    is_valid = controller.validate_file(file=file)
    if not is_valid[0]:
        return JSONResponse(
            content={
                "signal": ResponseEnum.ERROR.value, 
                "message": is_valid[1].value}
            ) 
    
    file_path = controller.generate_filename(
        original_filename=file.filename,
        project_id=project_id
    )


    try:
        
        async with aiofiles.open(file_path, 'wb') as out_file:
            while chunk := await file.read(app_settings.DEFAULT_CHUNK_SIZE):
                await out_file.write(chunk)
    except Exception as e:
        logger.error(f"error saving file: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "signal": ResponseEnum.file_valid.value, 
                "message": f"An error occurred while saving the file: {str(e)}"
            }
        )
    return JSONResponse(
        content={
            "signal": ResponseEnum.SUCCESS.value, 
            "message": "File uploaded successfully."}
        )