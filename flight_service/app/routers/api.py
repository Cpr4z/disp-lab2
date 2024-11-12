from fastapi import APIRouter

from flight_service.app.routers import flight, airport, manage


router = APIRouter()
router.include_router(flight.router)
router.include_router(airport.router)
router.include_router(manage.router)