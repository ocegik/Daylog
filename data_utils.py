# data_utils.py
import json
from colorama import Fore

def write_data(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(Fore.RED + "Data Saved Successfully.")
    except Exception as e:
        print(Fore.RED + f"An error occurred while writing to the file: {e}")

def read_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(Fore.RED + "File not found.")
        return {"users": []}
    except json.JSONDecodeError:
        print(Fore.RED + "Error decoding JSON.")
        return {"users": []}