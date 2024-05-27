import enum

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from database import Base
from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship, mapped_column, Mapped


# class Keyword(Base):
#     __tablename__='keyword'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     team


class Teams(Base):
    __tablename__ = 'teams'

    id: Mapped[int] = mapped_column(primary_key=True)
    team: Mapped[int]
    keyword: Mapped[str]
    # users = relationship("Users", back_populates="team")

    def __str__(self):
        return f"Команда {self.team}"

class Gender(str, enum.Enum):
    male='М'
    female='Ж'

class Category(str, enum.Enum):
    new= "Новичок"
    middle= "Любитель"
    profi= 'Профи'

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    runner: Mapped[int]
    hashed_password: Mapped[str]
    runner_category=Column('категория',Enum('Новичок',"Любитель","Профи", name='категория'),nullable=False)
    team_id=Column(Integer,ForeignKey('teams.id'))
    # team=relationship('Teams',back_populates='users')
    runner_gender=Column('пол',Enum('М','Ж', name='gender_enum'),nullable=False)
    zabeg22: Mapped[bool] = mapped_column(default=False,server_default="0")
    zabeg23: Mapped[bool]= mapped_column(default=False,server_default="0")
    # is_superuser=Column(bool, default=False)
    # is_active: bool
    # is_verified: bool

    def __str__(self):
        return f"Номер участника {self.runner}"
