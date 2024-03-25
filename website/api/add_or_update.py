import requests
from requests.auth import HTTPBasicAuth
import time

counter = 0

def generate_unique_id():
    global counter
    timestamp = int(time.time() * 1000)  # Get current timestamp in milliseconds
    counter += 1
    unique_id = (timestamp << 16) | (counter % 65536)  # Combine timestamp and counter
    return unique_id

item_data = {
        "text": "What is the output of the following code?\n\nx = 10\ny = 5\nprint(x > y)",
        "options": [["True", "False", "Error", "None"]],
        "correct_answer": "True"
}

myId = generate_unique_id()
response = requests.put(f'http://localhost:5000/api/v1/{myId}', json=item_data, auth=HTTPBasicAuth('05992ccec183b09f19354ba55014c19b','6e9ffaebace7cb744324c0e8784a2c69'))

if response.status_code == 201:
    item = response.json()
    print('Quiz added or updated successfully:')
    print(f'questionId: {item["questionId"]}')
    print(f'text: {item["text"]}')
    print(f'options: {item["options"]}')
    print(f'correct_answer: {item["correct_answer"]}')
else:
    print('Error:', response.json())
