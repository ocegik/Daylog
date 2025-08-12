# reset_password.py
import bcrypt
from colorama import Fore
from utils import obscure_email
from email_utils import generate_verification_code, send_email_verification
from data_utils import read_data, write_data
from config import GLOBAL_FILE_PATH

def reset_password(username):
    data = read_data(GLOBAL_FILE_PATH)
    user = next((user for user in data["users"] if user["username"] == username), None)

    if user:
        email = user['email']
        reset_code = generate_verification_code()

        print(f"A reset code has been sent to your email address: {obscure_email(email)}")
        send_email_verification(email, username, reset_code)

        verification_code_input = input("Please enter the verification code sent to your email:\n ")
        if verification_code_input == reset_code:
            # Handle new password input here
            new_password = input("Enter your new password: \n").strip()
            hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            user['password'] = hashed_new_password.decode('utf-8')
            write_data(GLOBAL_FILE_PATH, data)
            print("Your password has been reset successfully. Please login again.")
        else:
            print(Fore.RED + "Incorrect verification code.")
    else:
        print(Fore.RED + "User not found.")