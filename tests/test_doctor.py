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


def test_get_doctors(client):
    response = client.get("/doctors", headers=headers)

    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert response_data["status"] == 1


def test_post_doctors(client):
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

def test_get_single_doctors(client):
    response = client.get("/doctors/1", headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert "get " in response_data['message']
    assert 1 == response_data['status']

def test_put_doctors(client):
    data = {
        "name": "doctor edited",
        "username": "doctor_edited_ba",
        "password": "edited123",
        "gender": "male",
        "birthdate": "2021-01-01",
        "work_start_time": "08:00:00",
        "work_end_time": "18:00:00",
    }

    response = client.put("/doctors/1", data=json.dumps(data), headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert " updated" in response_data['message']
    assert 1 == response_data['status']

def test_delete_doctors(client):
    response = client.delete("/doctors/1", headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert " deleted" in response_data['message']
    assert 1 == response_data['status']
