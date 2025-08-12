# Sunrise Journal and Budget App

## Overview

Sunrise is a command-line Python application for user authentication, journaling, and basic budget management. It allows users to sign up with email verification, log in securely, add/view journal entries, and manage budgets. Data is stored in a local JSON file, and passwords are hashed using bcrypt for security. Email verification and password resets are handled via SMTP with HTML templates.

## Features

- **User Authentication**:
  - Signup with username, email, gender, age, and strong password validation.
  - Email verification using OTP sent via SMTP (supports Outlook; configurable).
  - Login with password hashing (bcrypt).
  - Password reset via email OTP.

- **Journaling**:
  - Add timestamped journal entries with title and text.
  - View all personal journal entries.

- **Account Management**:
  - Delete account after password confirmation.

- **Security & Validation**:
  - Email format and MX record validation.
  - Password strength checks (length, digits, cases, special chars).
  - Color-coded console output using Colorama.

- **Other**:
  - OTP generation for verification.
  - HTML email templates using Jinja2.

## Requirements

- Python 3.8+
- Required libraries (install via `pip install -r requirements.txt`):
  - bcrypt
  - colorama
  - python-dotenv
  - jinja2
  - dnspython
  - smtplib (built-in, but ensure email config)
  
  Note: Some original imports like mysql.connector, matplotlib, and numpy are not used in the refactored code and can be omitted.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/sunrise-app.git
   cd sunrise-app
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Set up `detail.env`.
   - Fill in your SMTP credentials:
     ```
     EMAIL_ADDRESS=your_email@outlook.com
     EMAIL_PASSWORD=your_app_password
     ```
     Note: Use an app-specific password if using 2FA.

4. Set up the database:
   - Set up `userdata.json`. It starts as `{"users": []}`.

5. Create email template:
   - In a `templates/` folder, edit `email_template.html` with your HTML content (e.g., basic template for verification code).

## Usage

Run the main script:
```
python main.py
```

- **Welcome Page**: Choose to log in or sign up.
- **Signup**: Enter details; verify email with OTP.
- **Login**: Enter credentials; reset password if forgotten.
- **Post-Login Menu**:
  - Add/view journal entries.
  - View budget diary (WIP).
  - Log out or delete account.

Example flow:
1. Sign up with a new account.
2. Verify email.
3. Log in.
4. Add a journal entry.
5. View entries.
6. Log out.

## License
MIT License. See LICENSE file for details.
For questions, open an issue on GitHub.
MIT License. See LICENSE file for details.

For questions, open an issue on GitHub.
