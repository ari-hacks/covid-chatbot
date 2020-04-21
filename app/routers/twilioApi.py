from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/")
async def read():
    return [{"name": "Hello"}, {"name": "World"}]

@router.get("/health-check")
async def health():
    return {"message": "Healthy as fuck"}


