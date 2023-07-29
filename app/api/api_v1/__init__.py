from fastapi import APIRouter
from . import endpoints
from . import authendpoint

router = APIRouter()
router.include_router(endpoints.router, prefix="/items")
router.include_router(authendpoint.router, prefix="/authentication")
