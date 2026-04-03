try:
    from starlette.middleware.base import BaseHTTPMiddleware
    from starlette.requests import Request
    STARLETTE_AVAILABLE = True
except ImportError:
    STARLETTE_AVAILABLE = False
    BaseHTTPMiddleware = object  # Fallback so class definition doesn't crash

from .logger import logger


class TokenMonitorMiddleware(BaseHTTPMiddleware if STARLETTE_AVAILABLE else object):
    """
    Starlette/FastAPI middleware that logs every incoming request.
    Only functional if starlette is installed.
    """

    def __init__(self, app):
        if not STARLETTE_AVAILABLE:
            raise ImportError(
                "starlette is required to use TokenMonitorMiddleware. "
                "Install it with: pip install starlette"
            )
        super().__init__(app)

    async def dispatch(self, request, call_next):
        response = await call_next(request)
        logger.info(f"{request.method} {request.url} → {response.status_code}")
        return response
