from DataHandler import JsonHandler

import os

def create_profile_summary_table():
    data_handler = JsonHandler(data_type = "profile_summary")
    data_handler.create_table("raw\\2025-08-17_profile_summary.json")
    
def create_protected_char_data():
    this_folder = os.getcwd()
    for file in os.listdir(f"{this_folder}\\data\\raw\\protected_data"):
        data_handler = JsonHandler(data_type = "protected_char_data")
        data_handler.create_table(f"raw\\protected_data\\{file}")
        
create_protected_char_data()