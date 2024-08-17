from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def get_request(api_endpoint: str = "", query_parameters: str = ""):
    response = client.get(f'{api_endpoint}{query_parameters}')
    return response

def post_request(api_endpoint: str = "", payload: dict = None):
    response = client.post(url = f'{api_endpoint}',
                             json=[payload.dict() for payload in payload])
    return response