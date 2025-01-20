from fastapi.responses import JSONResponse

from app.api.app import app
from app.api.routers.health_check import health_router

JSONResponse.media_type = "application/json; charset=utf-8"

# Routers
app.include_router(health_router, tags=["Health Check"])
