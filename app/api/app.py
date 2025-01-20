import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

API_PREFIX = os.getenv("API_PREFIX")
API_NAME = os.getenv("API_NAME")
VERSION = "0.1.0"


@asynccontextmanager
async def lifespan(_: FastAPI):
    print("La aplicacion se ha iniciado correctamente....")
    yield
    print("La aplicacion se ha cerrado correctamente....")


app = FastAPI(
    title=f"{API_NAME}",
    description="Documentacion de la API para el proyecto de Desarrollo Web - UV 2025",
    version=VERSION,
    openapi_url=f"{API_PREFIX}/openapi.json",
    docs_url=f"{API_PREFIX}/docs",
    redoc_url=f"{API_PREFIX}/redoc",
    lifespan=lifespan,
)
