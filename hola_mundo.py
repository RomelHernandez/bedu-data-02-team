import requests


response = requests.get('https://bedu.org')

print(response.status_code)