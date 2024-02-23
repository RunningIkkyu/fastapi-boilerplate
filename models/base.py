import uuid

from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column  # pyright: ignore
from sqlalchemy.orm import Mapped


class BaseModel(object):
    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=uuid.uuid4,
        comment="Unique ID of the record",
        sort_order=-1,
    )


Base = declarative_base(cls=BaseModel)
