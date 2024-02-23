from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column  # type: ignore

from models.base import Base
from models.mixin import DatetimeMixin


class Pet(DatetimeMixin, Base):
    """
    Pets database model
    """

    __tablename__ = "pet"

    name: Mapped[str] = mapped_column(
        String(128), nullable=False, comment="name of the pet"
    )
    age: Mapped[int] = mapped_column(
        String(128), nullable=False, comment="age of the pet"
    )
    species: Mapped[str] = mapped_column(
        String(128), nullable=False, comment="species of the pet"
    )
