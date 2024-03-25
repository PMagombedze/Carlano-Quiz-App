import requests
from requests.auth import HTTPBasicAuth

item_data = {
        "text": "Which of the following is a built-in module in Python for working with dates and times?",
        "options": [["datetime", "math", "os", "random"]],
        "correct_answer": "datetime"
    }

response = requests.put(f'http://localhost:5000/api/v1/1', json=item_data, auth=HTTPBasicAuth('05992ccec183b09f19354ba55014c19b','6e9ffaebace7cb744324c0e8784a2c69'))

if response.status_code == 201:
    item = response.json()
    print('Quiz added or updated successfully:')
    print(f'questionId: {item["questionId"]}')
    print(f'text: {item["text"]}')
    print(f'options: {item["options"]}')
    print(f'correct_answer: {item["correct_answer"]}')
else:
    print('Error:', response.json())
