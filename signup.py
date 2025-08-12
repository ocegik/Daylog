# signup.py
import bcrypt
from colorama import Fore
from utils import valid_password
from email_utils import is_valid_email_format, has_mx_record, generate_verification_code, send_email_verification
from data_utils import read_data, write_data
from login import login
from user_menu import post_login_options

def signup(file_path):
    data = read_data(file_path)
    users = data.get("users", [])

    while True:
        username = input("Enter your New Username: \n").strip()

        if any(user["username"] == username for user in users):
            print(Fore.RED + "This username already exists. Choose another unique username.")
        else:
            break

    email = input("Enter your Email: \n").strip()
    if not is_valid_email_format(email):
        print("Invalid email format. Please enter a valid email address.")
        return
    if not has_mx_record(email):
        print("Email domain does not exist or is invalid. Please enter a valid email address.")
        return

    verification_code = generate_verification_code()
    send_email_verification(email, username, verification_code)
    verification_code_input = input("Please enter the verification code sent to your email: ")
    if verification_code != verification_code_input:
        print(Fore.RED + "Verification failed. Please sign up again.")
        return

    valid_genders = ["male", "female"]
    while True:
        gender = input("Enter your Gender (Male/Female): \n").strip().lower()
        if gender in valid_genders:
            break
        else:
            print("Enter a Valid Gender (Male/Female)")

    while True:
        try:
            age = input("Enter your Age: \n").strip()
            age = int(age)
            if 0 <= age <= 100:
                break
            else:
                print("Enter a Valid Age between 0 and 100.")

        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a numeric value for age.")

    while True:
        password = input("Enter your New Strong Password: \n").strip()
        valid, message = valid_password(password)
        if not valid:
            print(message)
            continue

        if password == username:
            print(Fore.RED + "Choose a strong password \n Username and Password should not be same")
            continue
        break

    hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user = {
        "username": username,
        "password": hash_password.decode('utf-8'),
        "gender": gender,
        "age": str(age),
        "email": email,
    }
    users.append(new_user)

    data_to_write = {"users": users}
    write_data(file_path, data_to_write)
    print("Signup successful. You can now login with your new credentials.")

    login(file_path)
    post_login_options(username)