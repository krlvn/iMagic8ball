from sqlalchemy import Column, String, BigInteger, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import functions

Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = 'users'

    id = Column('id', BigInteger, unique=True, nullable=False, primary_key=True,
                comment='ID of telegram user')
    language = Column('language', String(length=2),
                comment='Selected language')
    created_at = Column('created_at', DateTime(timezone=True), server_default=functions.now())

    def __repr__(self):
        return f'<User:{self.id}>'
