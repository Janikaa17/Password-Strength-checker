import re
import string

# Function to check if password is in the rockyou.txt wordlist
def is_common_password(password):
    try:
        with open("/usr/share/wordlists/rockyou.txt", "r", encoding="latin-1") as file:
            # Check if password is in the rockyou.txt list
            for line in file:
                if line.strip() == password:
                    return True
    except FileNotFoundError:
        print("rockyou.txt not found! Ensure it's available.")
    return False

# Function to check password strength
def check_password_strength(password):
    # Check if password is common (from rockyou.txt)
    if len(password) < 8:
        return "Password is too short. It must be at least 8 characters."
    
    if is_common_password(password):
        return "Password is too common. Try a different one."
    
    # Check for uppercase letter
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    
    # Check for lowercase letter
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    
    # Check for digit
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    
    # Check for special character
    if not any(char in string.punctuation for char in password):
        return "Password must contain at least one special character."
    
    # Password passed all checks
    return "Password is strong!"

# Main function to handle user input
def main():
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()

