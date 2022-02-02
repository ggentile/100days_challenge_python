import requests

parameters = {
    "amount": 50,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php?amount=50&type=boolean", params=parameters)

data = response.json()

question_data = data["results"]

