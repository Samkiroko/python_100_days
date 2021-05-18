import requests
import json

data = requests.get(
    "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")

# print(question_data.json()['question'])
question_data = data.json()["results"]
