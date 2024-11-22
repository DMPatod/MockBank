from fastapi import FastAPI

from src.api.controllers.v1.CurrenciesController import router

app = FastAPI(title="Mock Bank", version="0.0.1")

app.include_router(router, prefix="/api/v1")