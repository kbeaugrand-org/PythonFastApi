"""
For more information about how to create FastApis, go to: https://fastapi.tiangolo.com/#create-it
"""
from fastapi import Depends, FastAPI, Header, HTTPException

from .routers import items

api = FastAPI()

api.include_router(
    items.router, 
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
    )