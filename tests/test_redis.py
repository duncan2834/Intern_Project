import pytest
from db.redis_client import get_redis_client
from db.redis_client import RedisClient

@pytest.mark.asyncio
async def test_redis_set_get():
    redis = await get_redis_client()
    
    await redis.set("foo", "bar")
    value = await redis.get("foo")
    
    assert value == "bar"


def test_redis_singleton():
    client1 = RedisClient()
    client2 = RedisClient()

    assert client1 is client2, "RedisClient is not a singleton"
