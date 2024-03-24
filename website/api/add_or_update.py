import requests
from requests.auth import HTTPBasicAuth

item_data = {
      "text": "What is the capital of France?",
      "options": {
        "a": 'Rome', 
        "b": "London",
        "c": "Paris",
        "d": "Berlin"
      },
      "correctAnswer": "Paris",

}

response = requests.put(f'http://localhost:5000/api/v1/3', json=item_data, auth=HTTPBasicAuth('percy_magom','6e9ffaebace7cb744324c0e8784a2c69'))

if response.status_code == 201:
    item = response.json()
    print('Quiz added or updated successfully:')
    print(f'questionId: {item["questionId"]}')
    print(f'text: {item["text"]}')
    print(f'options: {item["options"]}')
else:
    print('Error:', response.json())
