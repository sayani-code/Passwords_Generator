# generator.py

import random
import string


def generate_passwords(count, length, lower, upper, numbers, symbols):  #Generate  passwords

    all_characters = ""
    required = []

    if lower in ("y", "yes"):
        all_characters += string.ascii_lowercase
        required.append(random.choice(string.ascii_lowercase))

    if upper in ("y", "yes"):
        all_characters += string.ascii_uppercase
        required.append(random.choice(string.ascii_uppercase))

    if numbers in ("y", "yes"):
        all_characters += string.digits
        required.append(random.choice(string.digits))

    if symbols in ("y", "yes"):
        all_characters += string.punctuation
        required.append(random.choice(string.punctuation))

    passwords = []

    for _ in range(count):
        password = required.copy()

        while len(password) < length:
            password.append(random.choice(all_characters))

        random.shuffle(password)

        passwords.append("".join(password))
     
    return passwords

def check_password_strength(password):  #Check the strength of a password.

    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    score = sum([has_lower, has_upper, has_digit, has_symbol])

    if len(password) >= 12 and score == 4:
        return "Strong "
    elif len(password) >= 8 and score >= 3:
        return "Medium "
    else:
        return "Weak "