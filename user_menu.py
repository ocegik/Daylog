# user_menu.py
from utils import get_user_response
from journal import add_journal_entry, view_journal_entries
from account_delete import deleting_account
from config import GLOBAL_FILE_PATH

def post_login_options(username):
    print(f"What would you like to do next, {username}?")
    while True:
        print("\nOptions:")
        print("1. Add a new journal entry")
        print("2. View my journal entries")
        print("3. See Budget Diary")
        print("4. Log out")
        print("5. Delete account")

        choice = input("What would you like to do: \n")
        if choice == "1":
            add_journal_entry(username, file_path=GLOBAL_FILE_PATH)
        elif choice == "2":
            view_journal_entries(username, file_path=GLOBAL_FILE_PATH)
        elif choice == "4":
            print("You have successfully logged out.")
            break
        elif choice == "5":
            option = get_user_response("Are you sure you want to delete your account? (YES/NO)\n").lower().strip()
            if option == "yes":
                deleting_account(GLOBAL_FILE_PATH, username)
                break
            elif option == "no":
                print("Ok Taking you back")
                post_login_options(username)
            else:
                print("Enter appropriate response")
        else:
            print("Enter appropriate response")