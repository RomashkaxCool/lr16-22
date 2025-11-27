import datetime
import logging

import sentry_sdk
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/common", tags=["Common"])

logger = logging.getLogger(__name__)


@router.get("/healthcheck")
def healthcheck():
    logger.info("[COMMON][HEALTHCHECK] Service health check called")
    return {"status": "ok", "message": "Service is running"}


@router.get("/time")
def get_time():
    logger.info("[COMMON][TIME] Get server time")
    try:
        now = datetime.datetime.now().isoformat()
        logger.debug(f"[COMMON][TIME] current time={now}")
        return {"server_time": now}
    except Exception as e:
        logger.exception("[COMMON][TIME] error")
        sentry_sdk.capture_exception(e)
        raise HTTPException(500, "Failed to get server time")
