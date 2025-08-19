import pandas as pd
import json
import os

class JsonHandler:
    
    def __init__(self, data_folder: str = f"{os.getcwd()}\\data"):
        self.data_folder = data_folder
    
    def explore_profile_summary(self, data:dict):
        # First, let's isolate the account from the answer 
        wow_accounts = data["wow_accounts"]
        for account in wow_accounts:
            for character in account["characters"]:
                print(character)
        # TODO: return a list

    def create_table(self, file:str):
        print(f"{self.data_folder}\\{file}")
        
        with open(f"{self.data_folder}\\{file}", "r", encoding="utf8") as raw_data:
            json_data = json.load(raw_data)
            if "profile_summary" in file:
                self.explore_profile_summary(json_data)