from fastapi.testclient import TestClient

from core.config import settings
from main import app

client = TestClient(app)


def get_request(api_endpoint: str = "", query_parameters: str = ""):
    response = client.get(
        f"{api_endpoint}{query_parameters}",
        headers={"Authorization": f"Bearer {settings.auth_token}"},
    )
    return response


def post_request(api_endpoint: str = "", payloads: dict = None):
    response = client.post(
        url=f"{api_endpoint}",
        headers={"Authorization": f"Bearer {settings.auth_token}"},
        json=[payload.dict() for payload in payloads],
    )
    return response


def put_request(api_endpoint: str = "", payloads: dict = None):
    response = client.put(
        url=f"{api_endpoint}",
        headers={"Authorization": f"Bearer {settings.auth_token}"},
        json=[payload.dict() for payload in payloads],
    )

    return response


def delete_request(api_endpoint: str = "", payloads: dict = None):
    response = client.request(
        method="DELETE",
        url=f"{api_endpoint}",
        headers={"Authorization": f"Bearer {settings.auth_token}"},
        json=[payload.dict() for payload in payloads],
    )

    return response
