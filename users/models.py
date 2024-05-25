from database import Base
from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String, ForeignKey
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

    def __str__(self):
        return f"Номер {self.team}"

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    runner: Mapped[int]
    runner_team: Mapped[list['Teams']] = relationship(back_populates='user')
    runner_category: Mapped[int]
    team_id=Column(Integer,ForeignKey('teams.id'))
    runner_gender: Mapped[str]
    zabeg22: Mapped[bool]
    zabeg23: Mapped[bool]

    def __str__(self):
        return f"Номер {self.runner}"
