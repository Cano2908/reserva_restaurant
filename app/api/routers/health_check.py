from fastapi import APIRouter


health_router = APIRouter(prefix="/health_check")

@health_router.get("/")
async def health_check():
    return {"status": "ok"}