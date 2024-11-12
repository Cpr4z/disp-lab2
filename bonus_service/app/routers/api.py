from fastapi import APIRouter

from bonus_service.app.routers import privilege, privilege_history, manage


router = APIRouter()
router.include_router(privilege.router)
router.include_router(privilege_history.router)
router.include_router(manage.router)