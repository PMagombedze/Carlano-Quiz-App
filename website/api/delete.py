import requests
import json

QUESTION_API_URL = "http://127.0.0.1:5000/api/v1/python/"

def delete_question(question_data):
    headers = {"Content-Type": "application/json"}
    response = requests.request("DELETE", QUESTION_API_URL, headers=headers, data=json.dumps(question_data))
    if response.status_code == 200:
        return response.json()
    else:
        return {"success": False, "error": "Failed to delete question"}

# Example usage
question_data = {
        "correct_answer": "8",
        "id": 2,
        "options": [
            "5",
            "3",
            "8",
            "Error"
        ],
        "question": "What is the output of the following code?\n\nx = 5\ny = x + 3\nprint(y)"
    }

result = delete_question(question_data)
print(result)