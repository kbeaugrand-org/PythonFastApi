from fastapi import Depends, FastAPI, Header, HTTPException

from .routers import predict

app = FastAPI()

app.include_router(predict.router)