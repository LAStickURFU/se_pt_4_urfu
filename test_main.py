from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_redirect_to_documentation():
    response = client.get("/")
    print(response)
    assert response.status_code == 200
    assert "FastAPI - Swagger UI" in response.text


def test_shorten_text_positive():
    response = client.post("/shorten_text",
                           json={
                               "original_text": "some string"
                           })
    json_data = response.json()
    assert response.status_code == 200
    assert "some string" in json_data['short_text']


def test_shorten_text_negative():
    response = client.post("/shorten_text",
                           json={
                               "original_text": "some string"
                           })
    json_data = response.json()
    assert response.status_code == 200
    assert "bla bla" not in json_data['short_text']
