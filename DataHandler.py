import pandas as pd
import json
import os

class JsonHandler:
    
    def __init__(self, data_folder: str = f"{os.getcwd()}\\data", data_type:str=None):
        self.data_folder = data_folder
        self.data_type = data_type
    
    def _explore_profile_summary(self, data:dict):
        mes_persos = []
        # First, let's isolate the account from the answer 
        wow_accounts = data["wow_accounts"]
        for account in wow_accounts:
            for character in account["characters"]:
                perso = []
                # Href
                perso.append(character["character"]["href"])
                # Faction
                perso.append(character["faction"]["name"])
                # Genre
                if character["gender"]["type"] == "FEMALE":
                    perso.append("F")
                else:
                    perso.append("M")
                # id
                perso.append(character["id"])
                # niveau
                perso.append(character["level"])
                # nom
                perso.append(character["name"])
                # classe
                perso.append(character["playable_class"]["name"])
                # race
                perso.append(character["playable_race"]["name"])
                # référence protégée
                perso.append(character["protected_character"]["href"])
                # nom du royaume
                perso.append(character["realm"]["name"])
                mes_persos.append(perso)
        return mes_persos

    def _generate_table(self, data:list, columns:list):
        df = pd.DataFrame(data, columns=columns)
        return df

    def create_table(self, file:str):
        print(f"{self.data_folder}\\{file}")
        
        with open(f"{self.data_folder}\\{file}", "r", encoding="utf8") as raw_data:
            json_data = json.load(raw_data)
            if self.data_type == "profile_summary":
                columns = ["character_href","faction","gender","id","level","name","classe","race","protected_href","royaume"]
                data = self._explore_profile_summary(json_data)
            else:
                columns = []
                data = []
                
            df = self._generate_table(data, columns=columns)
            df.to_csv(f"{self.data_folder}\\tables\\{self.data_type}.csv", encoding="utf8")