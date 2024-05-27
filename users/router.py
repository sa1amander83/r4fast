from typing import Annotated

from fastapi import APIRouter, HTTPException, Form, Response, Depends

from users.auth import get_password_hash, authenticate_user, create_access_token
from users.dao import UserDAO
from users.dependecies import get_current_user
from users.exceptions import UserAlreadyExistsException, CannotAddDataToDatabase
from users.models import Users
from users.schemas import SUsers, SUsersLogin

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


@router_auth.post('/register')
# async def register_user(runner: Annotated[int, Form()], password: Annotated[str, Form()],
#                         team: Annotated[int, Form()], runner_category: Annotated[int, Form()],
#                         runner_gender: Annotated[str, Form()], zabeg22: Annotated[bool, Form()],
#                         zabeg23: Annotated[bool, Form()]):
async def register_user(user_data: SUsers):
    existing_user = await UserDAO.find_one_or_none(runner=user_data.runner)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    new_user = await UserDAO.add(runner=user_data.runner,
                                 hashed_password=hashed_password,
                                 team_id=user_data.team_id,
                                 runner_gender=user_data.runner_gender,
                                 runner_category=user_data.runner_category,
                                 zabeg22=user_data.zabeg22,
                                 zabeg23=user_data.zabeg23)
    if not new_user:
        raise CannotAddDataToDatabase


@router_auth.post("/login")
async def login_user(response: Response, user_data: SUsersLogin):
    user = await authenticate_user(user_data.runner, user_data.password)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("runner_access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router_auth.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("runner_access_token")


@router_users.get("/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user
