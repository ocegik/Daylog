# journal.py
from datetime import datetime
from data_utils import read_data, write_data

def add_journal_entry(username, file_path):
    title = input("Entry Title: \n")
    text = input("Your Entry: \n")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_entry = {
        "title": title,
        "text": text,
        "timestamp": timestamp
    }

    data = read_data(file_path)
    user_found = False
    for user in data['users']:
        if user['username'] == username:
            user_found = True
            if 'entries' not in user or type(user['entries']) is not list:
                user['entries'] = []  # This ensures 'entries' is initialized as a list
            user['entries'].append(new_entry)
            write_data(file_path, data)
            print("Journal entry added successfully.")
            break

    if not user_found:
        print("User not found. Unable to add journal entry.")

def view_journal_entries(username, file_path):
    data = read_data(file_path)
    user = next(user for user in data['users'] if user['username'] == username)
    entries = user.get('entries', [])

    for entry in entries:
        print(f"\nTitle: {entry['title']}")
        print(f"Timestamp: {entry['timestamp']}")
        print(f"Entry:\n{entry['text']}\n")