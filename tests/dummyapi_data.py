import requests
import faker

fake_data = faker.Faker()
fake_name, fake_lastName = fake_data.name().split()[0], fake_data.name().split()[1]
# fake_email = fake_data.email()

app_key = "65aba2b5f2a4c09c30ab2923"
base_url = "https://dummyapi.io/data/v1/"
dummyapi_headers = {
    "app-id":app_key
}

dummy_user_data = {
    "firstName" : fake_name,
    "lastName" : fake_lastName,
    "email" : fake_data.email()
}


