from typing import Union
from functools import lru_cache
from fastapi import Depends, FastAPI
from fastapi.middleware.gzip import GZipMiddleware
import config

from src.apis import apis
from src.prisma import prisma


app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.include_router(apis, prefix="/apis")

@lru_cache()
def get_settings():
    return config.Settings()

@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()

@app.get("/")
def read_root():
    return {"version": "1.0.0"}

@app.get("/documents")
async def get_documents():
  documents = await prisma.document.find_many()
  return {"documents": documents}

