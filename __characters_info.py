import json
import requests

# storage_space can be profile or data, data by default
# namespace_status can be static, dynamic or profile
# namespace_local can be us or eu
# database_source can be toy, realm
# region can us or eu
# index can "index" or an int

def request_token():
    data = {
        'grant_type': 'client_credentials',
    }

    access_token_request = requests.post('https://oauth.battle.net/token',
                            data=data, auth=('b48adf3f683d4114b756355e79ef0bd8', 'CdZ01qtxXmQ0LOmcToWvJ5HPyAT2Luj8'))
    
    access_token = access_token_request.json()

    return access_token['access_token']

def write_file(
        jsontext,
        database_source,
        index,
        characterName):
    
    if index == "index":
        json_dict = json.loads(jsontext)
        keys = json_dict.keys()
        # print(type(keys))
        parsed = json.dumps(json_dict[list(keys)[1]])
        with open(f'list_{database_source}.json',"w", encoding="utf8") as outfile:
            outfile.write(parsed)
    elif index != "index" and characterName:
        print(jsontext)
        with open(f'{characterName}_details.json',"w", encoding="utf8") as outfile:
            outfile.write(jsontext)
    else:
        print(jsontext)
        with open(f'{index}_details.json',"w", encoding="utf8") as outfile:
            outfile.write(jsontext)

def get_data(
        namespace_status,
        namespace_local,
        database_source,
        region="us",
        index="index",
        storage_space = "data",
        write_new_file = False,
        locale = None,
        characterName = None):
    
    access_token = request_token()

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # The data from the game is in the us servers and is static
    params = {
        'namespace': f'{namespace_status}-{namespace_local}',
        'locale':locale
    }

    # URL to get access to the API
    if locale:
        response = requests.get(
                f'https://{region}.api.blizzard.com/{storage_space}/wow/{database_source}/{index}', params=params, headers=headers)
    elif characterName:
        response = requests.get(
            f'https://{region}.api.blizzard.com/{storage_space}/wow/{database_source}/{index}/{characterName}', params=params, headers=headers)
    else:
        response = requests.get(
            f'https://{region}.api.blizzard.com/{storage_space}/wow/{database_source}/{index}', params=params, headers=headers)

    # print(response.status_code)
    if response.status_code == 200:
        if write_new_file:
            write_file(response.text,database_source,index,characterName)
        else:
            print(response.text)
    elif response.status_code == 403:
        print("Impossible to reach the server.")
    elif response.status_code == 404 and index.isdigit():
        print("This object does not exist")

# Get all the toys and put it in a json file
# get_data("static","us","toy",write_new_file=True)
        
#Get all the realms
# get_data("dynamic","us","realm",write_new_file=True)
        
# Get only Uldaman EU
# get_data("dynamic","eu","realm",region="eu",index="uldaman",locale="fr_EU",write_new_file=True)
        
#Get Vespasien
# get_data("profile", "eu", "character", region="eu", index="uldaman", locale="fr_EU", characterName="Vespasien")

get_data(
        "profile",
        "eu",
        "character",
        region="eu",
        index="uldaman",
        storage_space = "profile",
        write_new_file = True,
        locale = None,
        characterName = "vespasien")