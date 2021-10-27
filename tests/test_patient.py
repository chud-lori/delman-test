import json
import pytest
from werkzeug.wrappers import response
from app import create_app

app = create_app()

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4"
headers = {"Authorization": "{}".format(token), "Content-Type": "application/json"}


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_patients(client):
    response = client.get("/patients", headers=headers)

    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert response_data["status"] == 1


def test_post_patients(client):
    data = {
        "name": "patient new",
        "gender": "male",
        "birthdate": "2021-01-01",
        "no_ktp": "51710321121200017",
        "address": "Nangapanda"
    }

    response = client.post("/patients", data=json.dumps(data), headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 201
    assert "created" in response_data['message']
    assert 1 == response_data['status']

def test_get_single_patients(client):
    response = client.get("/patients/1", headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert "get " in response_data['message']
    assert 1 == response_data['status']

def test_put_patients(client):
    data = {
        "name": "patient new",
        "gender": "male",
        "birthdate": "2021-01-01",
        "no_ktp": "51710321121200017",
        "address": "Nangapanda",
        "vaccine_type": "sinovac",
        "vaccine_count": 1
    }

    response = client.put("/patients/1", data=json.dumps(data), headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert " updated" in response_data['message']
    assert 1 == response_data['status']

def test_delete_patients(client):
    response = client.delete("/patients/1", headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert " deleted" in response_data['message']
    assert 1 == response_data['status']
