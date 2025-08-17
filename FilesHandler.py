import os
from datetime import datetime
import json

class FilesHandler:
    
    def __init__(self):
        self.data_folder = f"{os.getcwd()}\\data\\"
    
    def save_file(self, data: dict, filename: str, format: str = "txt"):
        now = datetime.today().strftime('%Y-%m-%d')
        with open(f"{self.data_folder}{now}_{filename}.{format}", "w", encoding="utf8") as json_file:
            json.dump(data, json_file, sort_keys = True, indent = 4, ensure_ascii = False)