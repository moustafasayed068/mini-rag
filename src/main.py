from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from src.routers import base

app =  FastAPI()

app.include_router(base.router)