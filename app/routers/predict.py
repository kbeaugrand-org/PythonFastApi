from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/")
async def predict():
    return [{"name": "Item Foo"}, {"name": "item Bar"}]