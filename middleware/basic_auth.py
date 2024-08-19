import logging

from fastapi import HTTPException, Request
from fastapi.openapi.models import HTTPBearer
from starlette import status
from starlette.responses import JSONResponse

from core.config import settings

security = HTTPBearer

security_token = settings.auth_token


async def auth_middle_ware(request: Request, call_next):
    if request.url.path in ["/docs", "/openapi.json", "/redoc"]:
        return await call_next(request)

    try:
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Missing or Invalid Authorization header",
            )

        token = auth_header.split(" ")[1]
        if token != security_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

    except HTTPException as e:
        logging.error(f"Authentication failed {e.detail}")
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=e.detail)
    except Exception as e:
        logging.error(f"Unexpected error during authorization {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "Internal server error"},
        )

    return await call_next(request)
