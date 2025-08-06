from .endpoints import chat, search, list
from fastapi import APIRouter
from fastapi_healthchecks.checks.postgres import PostgreSqlCheck
from fastapi_healthchecks.checks.redis import RedisCheck
from fastapi_healthchecks.api.router import HealthcheckRouter, Probe

router = APIRouter()

router.include_router(chat.router, tags=["Chat"])
"""
router.include_router(search.router, prefix="/search", tags=["Search"])
router.include_router(list.router, prefix="/list", tags=["List"])
"""
router.include_router(
    HealthcheckRouter(
        Probe(
            name="liveness",
            checks=[
                
            ],
        ),
    ),
    prefix="/health",
)
