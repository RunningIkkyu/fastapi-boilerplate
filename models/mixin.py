from sqlalchemy import DATETIME, Column
from sqlalchemy.sql import func


class DatetimeMixin:
    created_at = Column(
        DATETIME,
        nullable=False,
        server_default=func.now(),
        comment="Record created time",
    )
    updated_at = Column(
        DATETIME,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
        comment="Record updated time",
    )
