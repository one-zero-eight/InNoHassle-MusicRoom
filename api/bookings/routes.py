from api.bookings import router
from api.dependencies import BOOKING_REPOSITORY_DEPENDENCY
from schemas import CreateBooking, ViewBooking


@router.post("/create_booking")
async def create_booking(
    participant_id: int,
    start_date: str,
    end_date: str,
    booking_repository: BOOKING_REPOSITORY_DEPENDENCY,
) -> ViewBooking:
    created = await booking_repository.create()
    return created


@router.get("/get_bookings_for_current_week")
async def get_bookings_for_current_week(
    booking_repository: BOOKING_REPOSITORY_DEPENDENCY,
) -> list[ViewBooking]:
    bookings = await booking_repository.get_bookings_for_current_week()
    return bookings
