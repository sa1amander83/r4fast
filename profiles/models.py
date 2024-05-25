from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Time, Computed, Numeric, Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date, time

from sqlalchemy.testing.pickleable import User

from database import Base

if TYPE_CHECKING:
    # Убирает предупреждения отсутствия импорта и неприятные подчеркивания в
    # PyCharm и VSCode
    from users.models import Users


class RunnerDay(Base):
    __tablename__ = 'profiles'

    id: Mapped[int] = mapped_column(primary_key=True)
    runner: Mapped[list['Users']] = relationship(back_populates='runnerday')
    runner_id= Column(Integer, ForeignKey('users.id'))
    day_select: Mapped[date] = mapped_column(Date())
    day_distance: Mapped[float] = mapped_column(Float)
    day_time: Mapped[time] = mapped_column(Time(timezone=True))
    day_average_temp: Mapped[time] = mapped_column(Time(timezone=True))

    def __str__(self):
        return str(self.runner)


class Statistic(Base):
    __tablename__ = 'statistic'
    id: Mapped[int] = mapped_column(primary_key=True)
    runner_id= Column(Integer, ForeignKey('users.id'))
    runner = relationship(User, back_populates='runnerday')
    total_distance: Mapped[float] = mapped_column(Float)
    total_time: Mapped[time] = mapped_column(Time(timezone=True))
    avg_time: Mapped[time] = mapped_column(Time(timezone=True))

    def __str__(self):
        return str(self.runner)
