from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from bot.settings import *

db_url = URL.create(DATABASE['DRIVER'],
                    DATABASE['USER'],
                    DATABASE['PASSWORD'],
                    DATABASE['HOST'],
                    DATABASE['PORT'],
                    DATABASE['NAME']
                    )
db_engine = create_async_engine(db_url, echo=False, future=True)
db_session = sessionmaker(db_engine, expire_on_commit=False, class_=AsyncSession)