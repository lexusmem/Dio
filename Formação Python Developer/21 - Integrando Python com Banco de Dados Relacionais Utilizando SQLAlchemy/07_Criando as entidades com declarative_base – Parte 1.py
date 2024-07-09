import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import interger
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class User(Base):
    __table_name__ = "user_account"
    # atibutos
    id = Column()
