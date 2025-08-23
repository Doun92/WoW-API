from BlizzardAPI import BlizzardApi
from FilesHandler import FilesHandler
from DataHandler import CSVHandler

# Connect to the objects
blizzard_api = BlizzardApi()
files_handler = FilesHandler()
data_handler = CSVHandler()

def get_profile_summary():
    code = input("Code temporaire: ")
    redirect_uri = "http://localhost:5000/callback"

    token_data = blizzard_api.exchange_code_for_token(code, redirect_uri)
    print("Token reçu :", token_data)

    profile_summary = blizzard_api.get_profile_summary()

    files_handler.save_file(profile_summary, "profile_summary", "json")

    # Si blizzard_api.get_profile_summary() ne fonctionne pas, je dois refaire
    # https://oauth.battle.net/authorize?client_id=<CLIENT_ID>&redirect_uri=http://localhost:5000/callback&response_type=code&scope=wow.profile

def get_protected_char_data():
    code = input("Code temporaire: ")
    redirect_uri = "http://localhost:5000/callback"
    
    token_data = blizzard_api.exchange_code_for_token(code, redirect_uri)
    print("Token reçu :", token_data)
    

    info = data_handler.get_protected_char_info()
    i= 0
    while i < len(info):
        data = info.loc[i, :].values.tolist()
        i+=1
        char_protected_data = blizzard_api.get_protected_character_summary(data[2],data[1])
        print(char_protected_data)
        files_handler.save_file(char_protected_data, f"{data[0]}_protected_data", "json")

# get_profile_summary()
get_protected_char_data()