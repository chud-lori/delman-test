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


def test_index(client):
    response = client.get("/")

    assert response.status_code == 404

def test_login(client):
    data = {
        "username": "admin",
        "password": "admin11132",
    }
    response = client.post("/login", data=json.dumps(data), headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert "success" in response_data['message']

def test_get_employees(client):
    response = client.get("/employees", headers=headers)

    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert response_data["status"] == 1


def test_post_employees(client):
    data = {
        "name": "employee new",
        "username": "employee_new_ba",
        "password": "new123",
        "gender": "male",
        "birthdate": "2021-01-01"
    }

    response = client.post("/employees", data=json.dumps(data), headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 201
    assert "created" in response_data['message']
    assert 1 == response_data['status']

def test_get_single_employees(client):
    response = client.get("/employees/1", headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert "get " in response_data['message']
    assert 1 == response_data['status']

def test_put_employees(client):
    data = {
        "name": "employee edited",
        "username": "employee_edited_ba",
        "password": "edited123",
        "gender": "male",
        "birthdate": "2021-01-01"
    }

    response = client.put("/employees/1", data=json.dumps(data), headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert " updated" in response_data['message']
    assert 1 == response_data['status']

def test_delete_employees(client):
    response = client.delete("/employees/1", headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert " deleted" in response_data['message']
    assert 1 == response_data['status']



# def test_distance_not_found(client):
#     response = client.get('/?destination=jakarta')

#     data = json.loads(response.get_data(as_text=True))
#     assert response.status_code == 404
#     assert data['status'] == 2

# def test_route_not_found(client):
#     response = client.get('/random')

#     assert response.status_code == 404
#     assert b'NOT FOUND' in response.data

# def test_inside_origin(client):
#     response = client.get('/?destination=moscow')

#     data = json.loads(response.get_data(as_text=True))

#     assert response.status_code == 200
#     assert data['status'] == 3

# def test_destination_empty(client):
#     response = client.get('/?destination=')

#     assert response.status_code == 302
