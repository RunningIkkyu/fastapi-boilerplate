import time
from uuid import uuid4

import sentry_sdk
from fastapi import HTTPException, Request
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


class RequestMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app,
    ):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        hex = str(uuid4().hex)
        request_id = f"req_{hex}"
        with logger.contextualize(request_id=request_id):
            logger.info(
                f"Incoming Request: {request.method}, {request.url}",
                extra={"url": request.url},
            )
            start_time = time.time()
            try:
                response = await call_next(request)
            except HTTPException as e:
                logger.warning(
                    f"Invalid request: {request.method}, {request.url}, status_code: {e.status_code}",
                    url=request.url,
                    status_code=e.status_code,
                )
                response = JSONResponse(content=e.detail, status_code=e.status_code)
                return response
            except Exception as e:
                logger.error(
                    f"Request failed: {request.method}, {request.url}",
                    url=request.url,
                )
                logger.exception(e)
                sentry_sdk.capture_exception(e)
                response = JSONResponse(content={"success": False}, status_code=500)
                return response
            process_time = time.time() - start_time
            response.headers["X-Request-ID"] = request_id
            logger.info(
                f"Request ended, process_time: {process_time}", reques_id=request_id
            )
            return response
