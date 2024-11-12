from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from uuid import UUID

from ticket_service.app.models.ticket import TicketModel
from ticket_service.app.schemas.ticket import TicketFilter, TicketUpdate
from ticket_service.app.enums.sort import SortTicket


class ITicketCRUD(ABC):
    def __init__(self, db: Session):
        self._db = db

    @abstractmethod
    async def get_all(
            self,
            ticket_filter: TicketFilter,
            sort_field: SortTicket,
            offset: int = 0,
            limit: int = 100
    ) -> list[TicketModel]:
        pass

    @abstractmethod
    async def get_by_uid(self, ticket_uid: UUID) -> TicketModel | None:
        pass

    @abstractmethod
    async def add(self, ticket: TicketModel) -> TicketModel | None:
        pass

    @abstractmethod
    async def delete(self, ticket: TicketModel) -> TicketModel:
        pass

    @abstractmethod
    async def patch(
            self,
            ticket: TicketModel,
            ticket_update: TicketUpdate
    ) -> TicketModel | None:
        pass