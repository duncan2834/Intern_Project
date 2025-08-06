import pytest
from db.postgres_client import get_pg_session
from sqlalchemy import text

@pytest.mark.asyncio
async def test_postgres_connection():
    async for session in get_pg_session():
        result = await session.execute(text("SELECT 1"))
        assert result.scalar() == 1
