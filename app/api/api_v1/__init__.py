from fastapi import APIRouter
from . import item
from . import auth

router = APIRouter()
router.include_router(item.router, prefix="/items")
router.include_router(auth.router, prefix="/authentication")
