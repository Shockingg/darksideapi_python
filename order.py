import requests

API_BASE_URL = 'https://darksidepanel.com/api/v2' 

def send_order(api_key, service_id, quantity, link, drip_feed=False):
    url = f'{API_BASE_URL}/orders/create'
    payload = {
        'api_key': api_key,
        'service_id': service_id,
        'quantity': quantity,
        'link': link
    }
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        order_id = response.json().get('order')
        print(f'Success! Order ID: {order_id}')
    else:
        print(f'Error: {response.status_code} - {response.text}')

# Get user input
api_key = input('Enter API key: ')
service_id = input('Enter service ID: ')
quantity = input('Enter quantity: ')
link = input('Enter link: ')

# Send the order
send_order(api_key, service_id, quantity, link)
