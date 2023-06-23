from __future__ import annotations

from sqlalchemy import String, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    scoped_session,
    sessionmaker,
)

engine = create_engine("sqlite:///db.sqlite")
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


class Base(DeclarativeBase):
    query = db_session.query_property()


class TestModel(Base):
    __tablename__ = "test_model"
    id: Mapped[str] = mapped_column(String(12), primary_key=True)
