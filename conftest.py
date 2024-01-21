import pytest
import requests
from tests.dummyapi_data import base_url, app_key, dummyapi_headers, dummy_user_data

@pytest.fixture(scope="module")
def create_delete_dummy_user():
    print("Creating new user for test...")
    create_user_result = requests.post(url=base_url + "user/create", data=dummy_user_data, headers=dummyapi_headers)
    new_user_id = create_user_result.json().get("id")
    yield create_user_result
    print("deleting tested user...")
    delete_user_result = requests.delete(url=base_url + f"user/{new_user_id}", headers=dummyapi_headers)
    print(delete_user_result.status_code)
    print(delete_user_result.text)


