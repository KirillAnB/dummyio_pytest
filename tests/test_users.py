import pytest
import requests
from dummyapi_data import app_key, base_url, dummyapi_headers, dummy_user_data


def test_user_create(create_delete_dummy_user):
    print(create_delete_dummy_user.text)
    assert create_delete_dummy_user.status_code == 200
    assert create_delete_dummy_user.json().get("firstName") == dummy_user_data.get("firstName")
    assert create_delete_dummy_user.json().get("lastName") == dummy_user_data.get("lastName")
    assert create_delete_dummy_user.json().get("email") == dummy_user_data.get("email")


def test_get_user_by_id(create_delete_dummy_user):
    user_id = create_delete_dummy_user.json().get("id")
    result = requests.get(url=base_url + f"user/{user_id}", headers=dummyapi_headers)
    print(result.text)

