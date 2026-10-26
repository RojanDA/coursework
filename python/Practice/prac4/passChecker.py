# Build a Python program that checks whether a given password is strong or weak based on certain rules.

import re
from datetime import datetime
import getpass
def is_strong_password(password):
    passwords = password.strip()
    length_error = len(passwords) < 8
    uppercase_error = not re.search(r'[A-Z]', passwords)  #or we can use = not any(passwords.isupper() for c in passwords)
    lowercase_error = not re.search(r'[a-z]', passwords) # or we can use = not any(passwords.islower() for c in passwords)
    digit_error = not re.search(r'\d', passwords)    # or we can use = not any(passwords.isdigit() for c in passwords)
    special_char_error = not re.search(r'[!@#$%^&*()_+=-`~{}|;:"<>,.?/]', passwords) 

    score = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])

    if score == 5:
        strength = "Strong password"
    elif score == 4:
        strength = "Medium password"
    elif score == 3:
        strength = "Weak password"
    else:
        strength = "Very weak password"
    

    feedback = []
    if length_error:
        feedback.append("Password must be at least 8 characters long.")
    if uppercase_error:
        feedback.append("Password must contain at least one uppercase letter.")
    if lowercase_error:
        feedback.append("Password must contain at least one lowercase letter.")
    if digit_error:
        feedback.append("Password must contain at least one digit.")
    if special_char_error:
        feedback.append("Password must contain at least one special character (e.g., !@#$%^&*()).")
    
    return strength, feedback

def save_log(password, strength, filename="password_log.txt"):
    with open(filename, 'a') as f:
        f.write(f"{datetime.now()} : Password: {password}\nStrength: {strength}\n\n")

def main():
    print("Welcome to the Password Strength Checker!")
    while True:
        password = getpass.getpass("Enter your password: ")
        strength, feedback = is_strong_password(password)
        print(f"Password Strength: {strength}")
        if feedback:
            print("Feedback:")
            for line in feedback:
                print(line)

        save_log(password, strength)

        if strength == "Strong":
            print("Your password is strong. You can use it.")
            break
        else:
            retry = input("Do you want to try another password? (y/n): ").lower()
            if retry == 'n':
                print("Thank you for using the Password Strength Checker!")
                break
            elif retry != 'y':
                print("Invalid input! Exiting the checker.")
                break

if __name__ == "__main__":
    main()

     

