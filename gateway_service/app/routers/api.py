from fastapi import APIRouter

from gateway_service.app.routers import gateway

router = APIRouter()
router.include_router(gateway.router)