from sqlalchemy import select

from dao.base import BaseDAO
from database import async_session_maker
from users.models import Users


class UserDAO(BaseDAO):
    model = Users
