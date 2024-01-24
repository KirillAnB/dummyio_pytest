import pytest
import requests
import allure
from tests.dummyapi_data import base_url, dummyapi_headers, dummy_user_data, fake_data

@allure.title("Creating test user with faker data and deleting it after test")
@pytest.fixture(scope="module")
def create_delete_dummy_user():
    body_for_test = dummy_user_data
    create_user_result = requests.post(url=base_url + "user/create", data=body_for_test, headers=dummyapi_headers)
    new_user_id = create_user_result.json().get("id")
    yield create_user_result, body_for_test
    print("deleting tested user...")
    delete_user_result = requests.delete(url=base_url + f"user/{new_user_id}", headers=dummyapi_headers)
    print(delete_user_result.status_code)
    print(delete_user_result.text)


@pytest.fixture(scope='function')
@allure.title("Creating test user with no deleting it")
def create_user():
    payload = {
        'firstName': fake_data.name().split()[0],
        'lastName' : fake_data.name().split()[1],
        'email' : fake_data.email()
    }
    create_user_result = requests.post(url=base_url + "user/create", data=payload, \
                                       headers=dummyapi_headers)
    test_user_id = create_user_result.json().get('id')
    print(create_user_result.text)
    return test_user_id
