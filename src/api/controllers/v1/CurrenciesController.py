from fastapi import APIRouter

from src.application.currencies.EcbUpdaterCurrency import EcbUpdaterCurrency

router = APIRouter(prefix="/currencies", tags=["currencies"])

@router.post("/")
async def update_currencies():
    updater = EcbUpdaterCurrency()
    temp = await updater.invoke()
    return 200