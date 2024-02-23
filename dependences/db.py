from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from database import Session as LocalSession


def get_db():
    db = LocalSession()
    return db


SessionDeps = Annotated[Session, Depends(get_db)]
