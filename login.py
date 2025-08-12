# login.py
import bcrypt
from colorama import Fore
from utils import get_user_response
from data_utils import read_data
from reset_password import reset_password

def login(file_path):
    data = read_data(file_path)
    username = input("Enter Your Username: \n").strip()
    # Attempt to find the user first
    user = next((user for user in data["users"] if user["username"] == username), None)

    if user is None:
        print(Fore.RED + "Invalid username.")
        return None

    # If user exists, proceed with password checking
    while True:
        password = input("Enter Your Password: \n").strip()
        if bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
            print(f"Welcome back {username}")
            return username

        print(Fore.RED + "Invalid Password.")
        response = get_user_response("Forgot Password? \nWant to Reset the password? (YES/NO) \n").strip().lower()
        if response == "yes":
            reset_password(username)
            return None
        elif response == "no":
            print(Fore.RED + "Try entering your password again.")