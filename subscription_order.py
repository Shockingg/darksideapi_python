import requests

API_BASE_URL = 'https://darksidepanel.com/api/v2' 

def send_order(api_key, service_id, username, quantity_min, quantity_max, link, posts=None, old_posts=None, delay=None, expiry=None):
    url = f'{API_BASE_URL}'
    payload = {
        'key': api_key,
        'action': 'add',
        'service': service_id,
        'username': username,
        'min': quantity_min,
        'max': quantity_max,
        'link': link,
        'posts': posts,
        'old_posts': old_posts,
        'delay': delay,
        'expiry': expiry
    }
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        order_id = response.json().get('order_id')
        print(f'Success! Order ID: {order_id}')
    else:
        print(f'Error: {response.status_code} - {response.text}')

# Get user input
api_key = input('Enter API key: ')
service_id = input('Enter service ID: ')
username = input('Enter username: ')
quantity_min = input('Enter quantity min: ')
quantity_max = input('Enter quantity max: ')
link = input('Enter link: ')
posts = input('Enter number of new posts (optional): ')
old_posts = input('Enter number of existing posts (optional): ')
delay = input('Enter delay in minutes: ')
expiry = input('Enter expiry date (optional - format: d/m/Y): ')

# Send the order
send_order(api_key, service_id, username, quantity_min, quantity_max, link, posts, old_posts, delay, expiry)
