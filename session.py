from alembic import context
from sqlalchemy import create_engine, engine_from_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


config = context.config
engine = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy."
)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


def commit_on_success(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        session.commit()
        return result

    return wrapper