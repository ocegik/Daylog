# account_delete.py
import bcrypt
from data_utils import read_data, write_data

def deleting_account(file_path, username):
    data = read_data(file_path)
    users = data.get("users", [])
    password = input("Please enter your password to confirm account deletion: \n").strip()

    for user in users:
        if user["username"] == username:
            stored_password_hash = user["password"].encode("utf-8")
            if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash):
                users.remove(user)
                write_data(file_path, {"users": users})
                print(f"Account for {username} has been successfully deleted.")
                break
            else:
                print("password incorrect. Account deletion cancelled")
                return False