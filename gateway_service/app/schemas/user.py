from pydantic import BaseModel

from gateway_service.app.schemas.ticket import TicketResponse
from gateway_service.app.schemas.bonus import PrivilegeShortInfo


class UserInfoResponse(BaseModel):
    tickets: list[TicketResponse]
    privilege: PrivilegeShortInfo