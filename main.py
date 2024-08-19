from fastapi.openapi.utils import get_openapi

from controllers.newsoutlet_controller import router as helloworld_router
from fastapi import FastAPI
import uvicorn
import logging

from core.config import settings
from middleware.basic_auth import auth_middle_ware


def custom_open_api():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=settings.OPENAPI_SCHEMA_NAME,
        version=settings.OPENAPI_SCHEMA_VERSION,
        summary=settings.OPENAPI_SCHEMA_SUMMARY,
        description="",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "Bearer Auth": {"type": "http", "scheme": "bearer"}
    }
    openapi_schema["security"] = [{"Bearer Auth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = FastAPI()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.getLogger("uvicorn.access").setLevel(logging.INFO)

app.include_router(helloworld_router)
app.middleware("http")(auth_middle_ware)
app.openapi = custom_open_api

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=5444,
        ssl_certfile="cert.pem",
        ssl_keyfile="key.pem",
        reload=True,
    )
