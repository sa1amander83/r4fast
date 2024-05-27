from datetime import datetime, timedelta
# from datetime import datetime

from jose import jwt
from passlib.context import CryptContext

from config import settings
from users.dao import UserDAO
from users.exceptions import IncorrectEmailOrPasswordException

pwd_context = CryptContext(schemes=['sha256_crypt'], deprecated='auto')


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=32)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    return encoded_jwt


async def authenticate_user(runner: int, password: str):
    user = await UserDAO.find_one_or_none(runner=runner)
    if not (user and verify_password(password, user.hashed_password)):
        raise IncorrectEmailOrPasswordException
    return user
