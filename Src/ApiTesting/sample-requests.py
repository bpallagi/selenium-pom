import requests
import json

BASE_URL = "https://api.github.com"
USER = "naveenkrnl"
# Making a GET request
request = requests.get(BASE_URL + '/users/' + USER)

# check status code for response received

assert request.status_code == 200
resp_body = request.json()
assert resp_body['login'] == 'naveenkrnl'
print(request)

print(BASE_URL + "/" + USER)
assert resp_body['html_url'] == 'https://github.com/' + USER

# success code - 200
print(request)

# print content of request
print(request.content)

response = requests.get('https://api.github.com/')
assert response.status_code == 200
# print request object
print(response.url)

# print status code
print(response.status_code)