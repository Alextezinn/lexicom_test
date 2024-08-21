from http import HTTPStatus

import redis
import pytest
import requests


client_redis = redis.Redis(host='localhost', port=6379, db=0)


def test_write_data_success():
    params = {
        "phone": "79381062015",
        "address": "Ленина 12"
    }

    response = requests.post("http://127.0.0.1:8000/write_data", json=params)
    assert response.status_code == HTTPStatus.CREATED
    assert client_redis.get(f"{params['phone']}").decode() == params['address']

    params = {
        "phone": "79381062015",
        "address": "Ленина 14"
    }

    response = requests.post("http://127.0.0.1:8000/write_data", json=params)
    assert response.status_code == HTTPStatus.OK
    assert client_redis.get(f"{params['phone']}").decode() == params['address']


def test_write_data_fail():
    params = {
        "phone": "7938106201",
        "address": "Ленина 12"
    }

    response = requests.post("http://127.0.0.1:8000/write_data", json=params)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_check_data_success():
    params = {
        "phone": "79371062015",
        "address": "Ленина 12"
    }

    requests.post("http://127.0.0.1:8000/write_data", json=params)

    response = requests.get(f"http://127.0.0.1:8000/check_data?phone={params['phone']}")
    assert response.status_code == HTTPStatus.OK


def test_check_data_fail():
    params = {
        "phone": "7937199999",
        "address": "Ленина 12"
    }

    requests.post("http://127.0.0.1:8000/write_data", json=params)

    response = requests.get(f"http://127.0.0.1:8000/check_data?phone={params['phone']}")
    assert "detail" in response.json()
