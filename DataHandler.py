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
                # Royaume
                perso.append(character["realm"]["id"])
                perso.append(character["realm"]["name"])
                mes_persos.append(perso)
        return mes_persos

    def _generate_table(self, data:list, columns:list):
        # print(data)
        # print(columns)
        df = pd.DataFrame(data, columns=columns)
        return df

    def _explore_protected_char_data(self, data:dict):
        stats = []
        stats.append(data["character"]["id"])
        stats.append(data["name"])
        
        # Argent (en cuivre)
        stats.append(data["money"])
        stats.append(data["protected_stats"]["level_gold_gained"])
        stats.append(data["protected_stats"]["level_gold_lost"])
        stats.append(data["protected_stats"]["total_gold_gained"])
        stats.append(data["protected_stats"]["total_gold_lost"])
        
        # Morts
        stats.append(data["protected_stats"]["level_number_deaths"])
        stats.append(data["protected_stats"]["total_number_deaths"])
        return stats        

    def create_table(self, file:str):
        with open(f"{self.data_folder}\\{file}", "r", encoding="utf8") as raw_data:
            json_data = json.load(raw_data)
            if self.data_type == "profile_summary":
                columns = ["character_href","faction","gender","id","level","name","classe","race","protected_href","royaume_id","royaume_nom"]
                data = self._explore_profile_summary(json_data)
                df = self._generate_table(data, columns=columns)
                df.to_csv(f"{self.data_folder}\\tables\\{self.data_type}.csv", encoding="utf8")
            elif self.data_type == "protected_char_data":
                columns = ["id","name","argent_en_cours","argent_gagné_niveau","argent_perdu_niveau","argent_gagné_total","argent_perdu_total","morts_niveau","morts_total"]
                data = self._explore_protected_char_data(json_data)
                
                # TODO: 
                # Il faut gérer toutes les csv dans pandas complet
                
                # df = self._generate_table(data, columns=columns)
                # df.to_csv(f"{self.data_folder}\\tables\\protected_data\\{json_data['name']}_{self.data_type}.csv", encoding="utf8")
            else:
                columns = []
                data = []
            
class CSVHandler:
    
    def __init__(self, data_folder: str = f"{os.getcwd()}\\data", data_type:str=None):
        self.data_folder = data_folder
        self.data_type = data_type
        
    def get_protected_char_info(self):
        # with open(f"{self.data_folder}\\tables\\profile_summary.csv", "r", encoding="utf8") as file:
        df = pd.read_csv(f"{self.data_folder}\\tables\\profile_summary.csv")
        return df[["name","id","royaume_id"]]