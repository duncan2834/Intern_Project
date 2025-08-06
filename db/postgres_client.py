# db/postgres_client.py

import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

class PostgresClient:
    instance = None
    engine = None
    session_maker = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(PostgresClient, cls).__new__(cls)

            DATABASE_URL = (
                f"postgresql+asyncpg://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
                f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
            )

            cls.engine = create_async_engine(
                DATABASE_URL,
                echo=False,
                pool_size=10,
                max_overflow=20,
                future=True,
            )
            cls.session_maker = sessionmaker(
                bind=cls.engine,
                class_=AsyncSession,
                expire_on_commit=False
            )
        return cls.instance

    def get_session(self) -> AsyncSession:
        return self.session_maker()
    
async def get_pg_session():
    db = PostgresClient()
    async with db.get_session() as session:
        yield session
