import requests
from dotenv import load_dotenv
import os

class BlizzardApi:
    
    def __init__(self):
        pass
    
    def __str__(self):
        return "Oui"
    
    def request_token(self):
        # Load secret .env file
        load_dotenv()
        
        # Define Crendetials
        AUTH_1 = os.getenv('AUTH_1')
        AUTH_2 = os.getenv('AUTH_2')
        
        data = {
            'grant_type': 'client_credentials',
        }

        access_token_request = requests.post('https://oauth.battle.net/token',
                                data=data, auth=(AUTH_1, AUTH_2))
        
        access_token = access_token_request.json()

        print(access_token['access_token'])

        return access_token['access_token']