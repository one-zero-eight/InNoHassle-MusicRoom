import datetime


def count_duration(start_time: datetime.datetime, end_time: datetime.datetime):
    duration = end_time - start_time
    seconds = duration.seconds
    minutes = seconds // 60
    hours = minutes / 60
    return hours


async def is_sc_working(start_time: datetime.datetime, end_time: datetime.datetime) -> bool:
    if start_time.hour < 7 or (end_time.hour > 22 and end_time.minute > 30):
        return False
    return True


async def is_offset_correct(booking_date: datetime.datetime) -> bool:
    current_datetime = datetime.datetime.now()
    if (booking_date - current_datetime).days > 7 or (booking_date - current_datetime).days < 0:
        return False
    return True


async def get_week_numbers(current_week: bool):
    today = datetime.datetime.now()

    offset = 0 if current_week else 7

    start_of_week = today - datetime.timedelta(days=today.weekday()) + datetime.timedelta(offset)

    current_week_dates = [start_of_week + datetime.timedelta(days=i) for i in range(7)]
    current_week_numbers = tuple(map(lambda date: date.day, current_week_dates))
    wide = current_week_numbers[2] > 9

    return current_week_numbers, wide
