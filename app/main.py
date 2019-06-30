from fastapi import Depends, FastAPI, Header, HTTPException

from .routers import items

app = FastAPI()

app.include_router(
    items.router, 
    prefix="/items",
    tags=["items"]
    )