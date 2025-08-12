# config.py
import os
from dotenv import load_dotenv
from colorama import init

init(autoreset=True)  # initializing colorama (to reset to normal color after command)

load_dotenv('detail.env')  # used to start loading environment from mentioned location or file
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')  # getting email address from env file
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')  # getting email password from env file
GLOBAL_FILE_PATH = "userdata.json"  # file path for database file