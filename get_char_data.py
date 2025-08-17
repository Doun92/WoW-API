from BlizzardAPI import BlizzardApi

# Connect to the object
blizzard_api = BlizzardApi()
print(blizzard_api.access_token)


code = "EUIKZRD7QQJGN34I4EKUM5GK68WXTIR867"
redirect_uri = "http://localhost:5000/callback"

token_data = blizzard_api.exchange_code_for_token(code, redirect_uri)
print("Token reçu :", token_data)

profile = blizzard_api.get_profile_summary()
# Si blizzard_api.get-profile_summary() ne fonctionne pas, je dois refaire
# https://oauth.battle.net/authorize?client_id=<CLIENT_ID&redirect_uri=http://localhost:5000/callback&response_type=code&scope=wow.profile