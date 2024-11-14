from fastapi import APIRouter

from routers import gateway, manage

router = APIRouter()
router.include_router(gateway.router)

health_router = APIRouter()
health_router.include_router(manage.router)