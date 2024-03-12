import requests

response = requests.delete('http://localhost:5000/items/1')

if response.status_code == 200:
    print('Item deleted successfully')
else:
    print('Error:', response.json())