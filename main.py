from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from app.routers import base

app =  FastAPI()

app.include_router(base.router)