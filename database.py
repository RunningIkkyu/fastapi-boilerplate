from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import create_database, database_exists

from models.base import Base
from settings import settings

engine = create_engine(
    f"mysql+pymysql://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}",
    pool_recycle=3600,
)

Session = scoped_session(sessionmaker(bind=engine))


def init_db():
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(engine)


init_db()
