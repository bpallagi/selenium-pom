import requests
import json
from jsonschema import validate
from jsonschema import Draft6Validator

BASE_URL = "https://api.github.com"
USER = "naveenkrnl"

schema = {
    "$schema": "https://json-schema.org/schema#",
    "type": "object",
    "properties": {
        "status": {
            "type": "string"
        },
        "employee": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string"
                },
                "firstName": {
                    "type": "string"
                },
                "middleName": {
                    "anyOf": [{
                        "type": "string"
                    }, {
                        "type": "null"
                    }]
                },
                "lastName": {
                    "type": "string"
                }
            },
            "required": ["id", "firstName", "lastName"]
        }
    }
}


def test_sample_get_response_code():
    response = requests.get('https://api.github.com/')
    assert response.status_code == 200
    print(response.url)
    print(response.status_code)


def test_sample_get_response_code_is_200():
    response = requests.get(BASE_URL + '/users/' + USER)
    assert response.status_code == 200
    print(response)
    print(response.content)


def test_sample_get_response_code_body():
    response = requests.get(BASE_URL + '/users/' + USER)
    resp_body = response.json()
    assert resp_body['login'] == 'naveenkrnl'
    assert resp_body['html_url'] == 'https://github.com/' + USER
    print(resp_body)


def test_get_employees_validates_json_resonse_schema():

    response = requests.get("https://api.github.com/")

    assert response.status_code == 200

    print(response.headers["Content-Type"])
    assert response.headers[
        "Content-Type"] == "application/json; charset=utf-8"

    resp_body = response.json()

    validate(instance=resp_body, schema=schema)