from sqlalchemy.orm import Session

from flight_service.app.models.flight import FlightModel
from flight_service.app.schemas.flight import FlightFilter, FlightCreate
from flight_service.app.exceptions.http_exceptions import NotFoundException, ConflictException
from flight_service.app.cruds.interfaces.flight import IFlightCRUD


class FlightService():
    def __init__(self, flightCRUD: type[IFlightCRUD], db: Session):
        self._flightCRUD = flightCRUD(db)

    async def get_all(
            self,
            flight_filter: FlightFilter,
            page: int = 1,
            size: int = 100
    ):
        return await self._flightCRUD.get_all(
            flight_filter=flight_filter,
            offset=(page - 1) * size,
            limit=size
        )

    async def get_by_id(self, flight_id: int):
        flight = await self._flightCRUD.get_by_id(flight_id)
        if flight == None:
            raise NotFoundException(prefix="Get flight")

        return flight

    async def add(self, flight_create: FlightCreate):
        flight = FlightModel(**flight_create.model_dump())
        flight = await self._flightCRUD.add(flight)
        if flight == None:
            raise ConflictException(
                prefix="Add flight",
                message="либо flight_number уже занят, " \
                        "либо такого(их) аэропорта(ов) не существует"
            )

        return flight

    async def delete(self, flight_id: int):
        flight = await self._flightCRUD.get_by_id(flight_id)
        if flight == None:
            raise NotFoundException(prefix="Delete flight")

        return await self._flightCRUD.delete(flight)