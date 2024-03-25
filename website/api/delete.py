import requests
from requests.auth import HTTPBasicAuth


response = requests.delete('http://localhost:5000/api/v1/0', auth=HTTPBasicAuth('05992ccec183b09f19354ba55014c19b','6e9ffaebace7cb744324c0e8784a2c69'))

if response.status_code == 200:
    print('Quiz deleted successfully')
else:
    print('Error:', response.json())