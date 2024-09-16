import requests

API_URL = 'https://api.exchangerate-api.com/v4/latest/'

def get_conversion_rate(from_currency, to_currency):
    response = requests.get(f'{API_URL}{from_currency}')
    if response.status_code == 200:
        data = response.json()
        return data['rates'].get(to_currency, None)
    return None