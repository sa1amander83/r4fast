from pydantic import BaseModel, ConfigDict


class SUsers(BaseModel):
    # id: int
    runner: int
    password: str
    runner_category: str
    team_id:int
    runner_gender: str
    zabeg22: bool
    zabeg23: bool
    # is_superuser: bool
    # is_active: bool
    # is_verified: bool
    model_config = ConfigDict(from_attributes=True)


class SUsersLogin(BaseModel):
    runner:int
    password:str
    model_config = ConfigDict(from_attributes=True)