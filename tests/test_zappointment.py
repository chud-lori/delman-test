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

def test_post_patients_additional(client):
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

def test_post_doctors_additional(client):
    data = {
        "name": "doctor new",
        "username": "doctor_new_ba",
        "password": "new123",
        "gender": "male",
        "birthdate": "2021-01-01",
        "work_start_time": "08:00:00",
        "work_end_time": "18:00:00",
    }

    response = client.post("/doctors", data=json.dumps(data), headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 201
    assert "created" in response_data['message']
    assert 1 == response_data['status']

def test_get_appointments(client):
    response = client.get("/appointments", headers=headers)

    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert response_data["status"] == 1


def test_post_appointments(client):
    data = {
        "doctor_id": "2",
        "patient_id": "2",
        "datetime": "2019-03-02 09:00:00",
        "status": "IN_QUEUE",
    }

    response = client.post("/appointments", data=json.dumps(data), headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 201
    assert "created" in response_data['message']
    assert 1 == response_data['status']

def test_get_single_appointments(client):
    response = client.get("/appointments/1", headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert "get " in response_data['message']
    assert 1 == response_data['status']

def test_put_appointments(client):
    data = {
        "doctor_id": "2",
        "patient_id": "2",
        "datetime": "2019-03-02 09:00:00",
        "status": "IN_QUEUE",
        "diagnose": "goodenough",
        "notes": "eatfruitmore"
    }

    response = client.put("/appointments/1", data=json.dumps(data), headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert " updated" in response_data['message']
    assert 1 == response_data['status']

def test_delete_appointments(client):
    response = client.delete("/appointments/1", headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert " deleted" in response_data['message']
    assert 1 == response_data['status']
