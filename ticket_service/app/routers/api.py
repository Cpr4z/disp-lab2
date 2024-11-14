from fastapi import APIRouter

from routers import ticket, manage


router = APIRouter()
router.include_router(ticket.router)

health_router = APIRouter()
health_router.include_router(manage.router)