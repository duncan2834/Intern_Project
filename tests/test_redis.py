import pytest
from db.redis_client import get_redis_client

@pytest.mark.asyncio
async def test_redis_set_get():
    redis = await get_redis_client()
    
    await redis.set("foo", "bar")
    value = await redis.get("foo")
    
    assert value == "bar"
