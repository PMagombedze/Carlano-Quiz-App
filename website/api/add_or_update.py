import requests

item_data = {
    'name': 'New Item2',
    'price': 12.46
}

response = requests.put('http://localhost:5000/items/2', json=item_data)

if response.status_code == 201:
    item = response.json()
    print('Item added or updated successfully:')
    print(f'ID: {item["id"]}')
    print(f'Name: {item["name"]}')
    print(f'Price: {item["price"]}')
else:
    print('Error:', response.json())
