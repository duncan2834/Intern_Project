import pytest
from db.postgres_client import get_pg_session
from db.postgres_client import PostgresClient
from sqlalchemy import text

@pytest.mark.asyncio
async def test_postgres_connection():
    async for session in get_pg_session():
        result = await session.execute(text("SELECT 1"))
        assert result.scalar() == 1

def test_postgres_singleton():
    client1 = PostgresClient()
    client2 = PostgresClient()

    assert client1 is client2, "PostgresClient is not a singleton"