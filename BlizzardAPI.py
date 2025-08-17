import requests
from dotenv import load_dotenv
from os import getenv

class BlizzardApi:
    
    def __init__(self):
        self.access_token = self._request_token()
        # self.oauth_token = self.exchange_code_for_token()
        self.basic_url = "https://eu.api.blizzard.com/"
        self.token_url = "https://oauth.battle.net/token"
    
    def __str__(self):
        return "Connecté"
    
    def _request_token(self):
        """
        Permet de générer une réponse JSON avec la clé d'accès à l'API publique.

        Returns:
            JSON: La clé d'accès à l'API publique
        """
        # Load secret .env file
        load_dotenv()
        
        # Define Crendetials
        client_id = getenv('Client_ID')
        client_secret = getenv('Client_Secret')
        
        data = {
            'grant_type': 'client_credentials',
        }

        access_token_request = requests.post('https://oauth.battle.net/token',
                                data=data, auth=(client_id, client_secret))
        
        access_token = access_token_request.json()
        return access_token
    
    def exchange_code_for_token(self, code:str, redirect_uri: str):
        """
        Échange un code temporaire contre un access_token utilisable.
        """
        # Load secret .env file
        load_dotenv()
        
        # Define Crendetials
        client_id = getenv('Client_ID')
        client_secret = getenv('Client_Secret')
        
        
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri
        }
        
        response = requests.post(
            self.token_url,
            data=data,
            auth=(client_id, client_secret)
        )
    
        if response.status_code != 200:
            raise Exception(f"Erreur {response.status_code}: {response.text}")

        token_data = response.json()
        print(token_data)
        self.access_token = token_data["access_token"]
        
        return token_data
    
    def get_profile_summary(self):
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        params = {
            "namespace": "profile-eu",
            "locale": "fr_FR"
        }
        
        url = f"{self.basic_url}/profile/user/wow"
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            raise Exception(f"Erreur {response.status_code}: {response.text}")

        return response.json()