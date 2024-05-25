from fastapi import APIRouter

from users.dao import UserDAO
from users.schemas import SUsers

router_auth = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

router_users = APIRouter(
    prefix="/users",
    tags=["Участники"],
)


# @router_users.get('')
# async def get_users():
#     return await UserDAO.get_all_users()


@router_users.get('')
async def show_profile() -> list[SUsers]:
    return await UserDAO.get_all_users()
