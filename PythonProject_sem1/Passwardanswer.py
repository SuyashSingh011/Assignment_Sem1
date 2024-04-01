import re

def validate_password(password, username, last_three_passwords):
    if len(password) < 10:
        return False, "Password must be at least 10 characters long."
    
    if not (any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in "!@#$%^&*" for c in password)):
        return False, "Password must contain at least two uppercase letters, two lowercase letters, two digits, and two special characters."

    
    if re.search(r'(.)\1\1\1', password):
        return False, "Password cannot contain any character repeated more than three times in a row."

    if any(username[i:i+3] in password for i in range(len(username) - 2)):
        return False, "Password cannot contain sequences of three or more consecutive characters from the username."

    # Check historical password check
    if password in last_three_passwords:
        return False, "Password cannot be the same as any of the last three passwords."

    return True, "Password meets all criteria."

def main():
    username = input("Enter username: ")
    last_three_passwords = []  #  user's last three passwords
    valid_password = False

    while not valid_password:
        password = input("Enter password: ")
        is_valid, message = validate_password(password, username, last_three_passwords)
        if is_valid:
            valid_password = True
            print("Password set successfully!")
        else:
            print(message)

if __name__ == "__main__":
    main()
