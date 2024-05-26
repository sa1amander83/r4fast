from pydantic import BaseModel, ConfigDict


class SUsers(BaseModel):
    # id: int
    runner: int
    password: str
    runner_category: int
    team_id:int
    runner_gender: str
    zabeg22: bool
    zabeg23: bool
    model_config = ConfigDict(from_attributes=True)