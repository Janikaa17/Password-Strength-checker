# Password Strength Checker

## Description
This is a Python program that checks the strength of a password. It evaluates passwords based on:
- Length (at least 8 characters).
- Presence of uppercase letters, lowercase letters, digits, and special characters.
- Checks against the common passwords list (Rockyou).

## Features
- Password length check
- Must contain at least one uppercase letter
- Must contain at least one lowercase letter
- Must contain at least one digit
- Must contain at least one special character
- Checks if the password is in the commonly used password list (`rockyou.txt`)

## Requirements
- Python 3.x
- `rockyou.txt` (usually found at `/usr/share/wordlists/rockyou.txt`)

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/password-strength-checker.git
   ```

2. Navigate to the project directory:
   ```bash
   cd password-strength-checker
   ```

3. Run the script:
   ```bash
   python3 password_strength_checker.py
   ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

