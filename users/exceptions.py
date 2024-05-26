from fastapi import HTTPException, status


class SiteException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(SiteException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


class IncorrectEmailOrPasswordException(SiteException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный логин или пароль"


class TokenExpiredException(SiteException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Срок действия токена истек"


class TokenAbsentException(SiteException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен отсутствует"


class IncorrectTokenFormatException(SiteException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"


class UserIsNotPresentException(SiteException):
    status_code = status.HTTP_401_UNAUTHORIZED


class RoomFullyBooked(SiteException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Не осталось свободных номеров"


class RoomCannotBeBooked(SiteException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Не удалось забронировать номер ввиду неизвестной ошибки"


class DateFromCannotBeAfterDateTo(SiteException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Дата заезда не может быть позже даты выезда"


class CannotBookHotelForLongPeriod(SiteException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Невозможно забронировать отель сроком более месяца"


class CannotAddDataToDatabase(SiteException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Не удалось добавить запись"


class CannotProcessCSV(SiteException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Не удалось обработать CSV файл"