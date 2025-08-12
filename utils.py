# utils.py
import string
from colorama import Fore

def get_user_response(prompt):
    while True:
        response = input(prompt).lower().strip()
        if response in ["yes", "no"]:
            return response
        else:
            print(Fore.RED + "Please give an appropriate response")

def valid_password(password):
    if len(password) < 8:
        return False, Fore.RED + "Password should be longer than 8 characters long."

    if not any(char.isdigit() for char in password):
        return False, Fore.RED + "Password must contain at least one digit"

    if not any(char.islower() for char in password):
        return False, Fore.RED + "Password must contain at least one lower case letter"

    if not any(char.isupper() for char in password):
        return False, Fore.RED + "Password must contain at least one upper case letter"

    if not any(char in string.punctuation for char in password):
        return False, Fore.RED + "Password must contain at least one special character"

    return True, Fore.GREEN + "password is valid"

def obscure_email(email):
    parts = email.split('@')
    local = parts[0]
    obscured_local = local[0] + "***" + local[-1] if len(local) > 2 else local
    return obscured_local + "@" + parts[1]