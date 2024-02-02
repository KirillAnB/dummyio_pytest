import faker
import requests
from dummyapi_data import base_url, dummyapi_headers
import random
import jsonschema


post_model = {
    "type":"object",
    "properties":{
        'text':{"type":"string"},
        'image':{'type':"string"},
        'owner':{"type":"object"},
        'likes':{"type":"number"}
    },
    'required':['owner']
}

def test_create_post(create_delete_dummy_user):
    user_id = create_delete_dummy_user[0].json().get("id")
    post_data = {
        'text' : faker.Faker().text(),
        'image': faker.Faker().url(),
        'owner': user_id,
        'likes': random.randint(1,99)

    }
    create_comment_result = requests.post(url=base_url + 'post/create', headers=dummyapi_headers, data=post_data)
    print(create_comment_result.text)
    assert create_comment_result.status_code == 200, "Status code is not 200"
    jsonschema.validate(create_comment_result.json(), post_model)



