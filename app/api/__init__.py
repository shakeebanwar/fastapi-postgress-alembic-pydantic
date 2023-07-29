from fastapi import APIRouter
from .api_v1 import endpoints as v1

router = APIRouter()
router.include_router(v1.router, prefix="/v1")
