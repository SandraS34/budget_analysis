from datetime import date

from sqlalchemy import Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import db


class Income(db.Model):
    __tablename__ = "income"

    id: Mapped[int] = mapped_column(primary_key=True)
    month: Mapped[date] = mapped_column(Date, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    amount_grosze: Mapped[int] = mapped_column(Integer, nullable=False)


class Expense(db.Model):
    __tablename__ = "expense"

    id: Mapped[int] = mapped_column(primary_key=True)
    month: Mapped[date] = mapped_column(Date, nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    amount_grosze: Mapped[int] = mapped_column(Integer, nullable=False)
