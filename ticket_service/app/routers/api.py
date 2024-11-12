from fastapi import APIRouter

from ticket_service.app.routers import ticket, manage


router = APIRouter()
router.include_router(ticket.router)
router.include_router(manage.router)