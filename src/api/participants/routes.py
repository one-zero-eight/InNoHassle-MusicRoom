from src.api.dependencies import Dependencies
from src.api.participants import router
from src.tools import get_date_from_str
from src.tools import max_hours_to_book_per_day as status_validate
from src.exceptions import InvalidDateFormat, InvalidParticipantStatus
from src.repositories.participants.abc import AbstractParticipantRepository
from src.schemas import FillParticipantProfile, ViewBooking, ViewParticipantBeforeBooking


@router.post("/fill_profile")
async def fill_profile(
    participant: FillParticipantProfile,
) -> ViewParticipantBeforeBooking:
    participant_repository = Dependencies.f(AbstractParticipantRepository)
    created = await participant_repository.fill_profile(participant)
    return created


@router.put("/{participant_id}/status")
async def change_status(
    participant_id: int,
    new_status: str,
) -> ViewParticipantBeforeBooking | str:
    participant_repository = Dependencies.f(AbstractParticipantRepository)

    try:
        status_validate(new_status)
    except InvalidParticipantStatus:
        raise InvalidParticipantStatus()

    updated_participant = await participant_repository.change_status(participant_id, new_status)
    return updated_participant


@router.get("/{participant_id}/bookings")
async def get_participant_bookings(participant_id: int) -> list[ViewBooking]:
    participant_repository = Dependencies.f(AbstractParticipantRepository)
    bookings = await participant_repository.get_participant_bookings(participant_id)
    return bookings


@router.get("/{participant_id}/remaining_weekly_hours")
async def get_remaining_weekly_hours(participant_id: int) -> float:
    participant_repository = Dependencies.f(AbstractParticipantRepository)
    ans = await participant_repository.remaining_weekly_hours(participant_id)
    return ans


@router.get("/{participant_id}/remaining_daily_hours")
async def get_remaining_daily_hours(participant_id: int, date: str) -> float:
    participant_repository = Dependencies.f(AbstractParticipantRepository)

    try:
        parsed_date = await get_date_from_str(date)
        ans = await participant_repository.remaining_daily_hours(participant_id, parsed_date)
    except ValueError:
        raise InvalidDateFormat()
    return ans


@router.get("/{participant_id}/phone_number")
async def get_phone_number(participant_id: int):
    participant_repository = Dependencies.f(AbstractParticipantRepository)

    return await participant_repository.get_phone_number(participant_id)


@router.get("/participant_id")
async def get_participant_id(telegram_id: str):
    participant_repository = Dependencies.f(AbstractParticipantRepository)

    res = await participant_repository.get_participant_id(telegram_id)
    return res
