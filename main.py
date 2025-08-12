# main.py
from colorama import Fore
from utils import get_user_response
from login import login
from signup import signup
from user_menu import post_login_options
from config import GLOBAL_FILE_PATH

def welcome_page():
    print("Welcome to our program")
    while True:
        response = get_user_response(Fore.GREEN+"Do you have a existing account? (YES/NO)\n").lower().strip()
        if response == "yes":
            username = login(GLOBAL_FILE_PATH)
            if username:
                post_login_options(username)
            break

        else:
            answer = get_user_response(Fore.YELLOW+"Do you want to make a account? (YES/NO)\n").lower().strip()
            if answer == "yes":
                signup(GLOBAL_FILE_PATH)
            elif answer == "no":
                print("Thanks for visiting. Exiting the program")
            break

def main():
    welcome_page()

if __name__ == "__main__":
    main()