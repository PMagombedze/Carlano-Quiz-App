import requests

question_data = {
    "question": "What is the capital of France?",
    "options": ["London", "Paris", "Berlin", "Madrid"],
    "correct_answer": "Paris",
    "id": 28
}

endpoint = "http://127.0.0.1:5000/api/v1/python/add"

response = requests.post(endpoint, json=question_data)

if response.status_code == 200:
    print("Question added successfully!")
else:
    print("Failed to add the question. Error:", response.text)