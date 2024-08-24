import requests

base_url = "https://flask-heroku-test-1-19ead2b012a7.herokuapp.com/"

# Test the helloworld resource
response = requests.put(base_url + "helloworld/John", json={"name": "John", "money": 12, "family": 4})
print(response.json())

response = requests.get(base_url + "helloworld/John")
print(response.json())
