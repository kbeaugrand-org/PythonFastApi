from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
async def get_items():
    return [{"name": "Item Foo"}, {"name": "item Bar"}]