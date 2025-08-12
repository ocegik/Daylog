# verification.py
from data_utils import read_data, write_data

def verify_email(file_path, username, input_code):
    data = read_data(file_path)
    for user in data['users']:
        if user['username'] == username and user.get('verification_code') == input_code:
            user['verified'] = True
            del user['verification_code']
            write_data(file_path, data)
            print("Email verified successfully!")
            return True
        print("Verification Failed!")
        return False