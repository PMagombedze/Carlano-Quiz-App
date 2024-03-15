import requests

response = requests.delete('http://localhost:5000/api/v1/4')

if response.status_code == 200:
    print('Quiz deleted successfully')
else:
    print('Error:', response.json())