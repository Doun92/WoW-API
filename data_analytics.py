from DataHandler import JsonHandler

data_handler = JsonHandler(data_type = "profile_summary")
data_handler.create_table("raw\\2025-08-17_profile_summary.json")