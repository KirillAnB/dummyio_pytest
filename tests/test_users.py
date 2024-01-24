import pytest
import requests
from dummyapi_data import  base_url, dummyapi_headers, fake_data




def test_user_create(create_delete_dummy_user):
    data_for_test = create_delete_dummy_user
    print(data_for_test)
    assert data_for_test[0].status_code == 200
    assert data_for_test[0].json().get("firstName") == data_for_test[1].get("firstName")
    assert data_for_test[0].json().get("lastName") == data_for_test[1].get("lastName")
    assert data_for_test[0].json().get("email") == data_for_test[1].get("email")


def test_get_user_by_id(create_delete_dummy_user):
    user_id = create_delete_dummy_user[0].json().get("id")
    result = requests.get(url=base_url + f"user/{user_id}", headers=dummyapi_headers)
    for key in create_delete_dummy_user[0].json():
        print(f"Cheking {key}")
        assert create_delete_dummy_user[0].json().get(key) == result.json().get(key)

def test_user_in_users_list(create_delete_dummy_user):
    user_id = create_delete_dummy_user[0].json().get("id")
    user_created = create_delete_dummy_user[0].json().get("registerDate")
    user_list = []
    for i in range(1,3):
        payload = {
        "registerDate" : {user_created},
        "limit" : 50,
        "page" : i
    }
        user_data_list = requests.get(url=base_url + "user", headers=dummyapi_headers, params=payload).json().get("data")
        user_list.append(user_data_list)
    user_found = False
    for item in user_list:
        for _dict in item:
            if _dict['id'] == user_id:
                user_found = True
                print(f"User was found on page {i}")
    assert user_found == True

@pytest.mark.parametrize('firstname, lastname',[(fake_data.name().split()[0], fake_data.name().split()[1])  for i in range(10)])
def test_update_user(create_delete_dummy_user, firstname, lastname):
    user_for_test = create_delete_dummy_user[0]
    payload = {
        "firstName" : firstname,
        "lastname" : lastname,
    }
    test_user_id = user_for_test.json().get("id")
    update_result = requests.put(url=base_url + f'user/{test_user_id}', data = payload, headers=dummyapi_headers)
    print(update_result.text)


def test_user_delete(create_user):
    user_id = create_user
    delete_result = requests.delete(url=base_url + f'user/{user_id}', headers=dummyapi_headers)
    print(delete_result.status_code)
    print(delete_result.text)

