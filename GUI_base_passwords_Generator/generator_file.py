# generator.py

import secrets
import string


def generate_passwords(count, length, lower, upper, numbers, symbols):#Generate one or more random passwords.

    character_sets = []

    if lower:
        character_sets.append(string.ascii_lowercase)

    if upper:
        character_sets.append(string.ascii_uppercase)

    if numbers:
        character_sets.append(string.digits)

    if symbols:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("Select at least one character type.")

    if length < len(character_sets):
        raise ValueError(
            "Password length is too short for the selected options."
        )

    all_characters = "".join(character_sets)
    passwords = []

    for _ in range(count):
        # Guarantee at least one character from every selected category
        password = [
            secrets.choice(character_set)
            for character_set in character_sets
        ]

        
        while len(password) < length:
            password.append(secrets.choice(all_characters))

        # Shuffle securely
        secrets.SystemRandom().shuffle(password)

        passwords.append("".join(password))

    return passwords


def check_password_strength(password):  #Check the strength of a password.

    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    score = sum([
        has_lower,
        has_upper,
        has_digit,
        has_symbol
    ])

    if len(password) >= 12 and score == 4:
        return "Strong"

    elif len(password) >= 8 and score >= 3:
        return "Medium"

    return "Weak"