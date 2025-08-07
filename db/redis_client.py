import os
from redis.asyncio import Redis 
from dotenv import load_dotenv

load_dotenv()

class RedisClient:
    instance = None
    pool: Redis = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    async def connect(self):
        if not self.pool:
            redis_url = f"redis://{os.getenv('REDIS_HOST')}:{os.getenv('REDIS_PORT')}"
            self.pool = Redis.from_url(
                redis_url,
                encoding="utf-8",
                decode_responses=True,
                max_connections=20,
            )

    def get_client(self) -> Redis:
        if not self.pool:
            raise Exception("Redis not connected. Call connect() first.")
        return self.pool

    async def close(self):
        if self.pool:
            await self.pool.close()
            self.pool = None

redis_client = RedisClient()

async def get_redis_client():
    await redis_client.connect()
    return redis_client.get_client()
