from BlizzardAPI import BlizzardApi
from FilesHandler import FilesHandler

# Connect to the objects
blizzard_api = BlizzardApi()
files_handler = FilesHandler()

def get_profile_summary():
    code = input("Code temporaire: ")
    redirect_uri = "http://localhost:5000/callback"

    token_data = blizzard_api.exchange_code_for_token(code, redirect_uri)
    print("Token reçu :", token_data)

    profile_summary = blizzard_api.get_profile_summary()

    files_handler.save_file(profile_summary, "profile_summary", "json")

    # Si blizzard_api.get_profile_summary() ne fonctionne pas, je dois refaire
    # https://oauth.battle.net/authorize?client_id=<CLIENT_ID>&redirect_uri=http://localhost:5000/callback&response_type=code&scope=wow.profile

get_profile_summary()



