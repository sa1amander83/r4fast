from fastapi import APIRouter

from users.dao import UserDAO

router = APIRouter(
    prefix='/profile',
    tags=['Профиль участника']
)


# @router.get('/{user_id}')
# async def show_profile(user_id):
#     return await UserDAO.find_one_or_none(1)
