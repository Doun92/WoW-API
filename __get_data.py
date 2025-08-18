import json
import requests


def request_token():
    data = {
        'grant_type': 'client_credentials',
    }

    access_token_request = requests.post('https://oauth.battle.net/token',
                            data=data, auth=('b48adf3f683d4114b756355e79ef0bd8', 'CdZ01qtxXmQ0LOmcToWvJ5HPyAT2Luj8'))
    
    access_token = access_token_request.json()

    return access_token['access_token']

def get_wow_token_price():
    access_token = request_token()

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    params = {
        'namespace': 'dynamic-eu',
    }

    response = requests.get(
        'https://eu.api.blizzard.com/data/wow/token/', params=params, headers=headers)

    print(response.status_code)
    print(response.text)


get_wow_token_price()
