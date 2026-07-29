# main.py

from utils import (
    get_password_count,
    get_password_length,
    get_user_choices,
)

from generator import generate_passwords, check_password_strength


def main():
    print("===== Password Generator =====")

    # Get user input
    count = get_password_count()
    length = get_password_length()
    lower, upper, numbers, symbols = get_user_choices()

    # Generate passwords
    passwords = generate_passwords(
        count,
        length,
        lower,
        upper,
        numbers,
        symbols
    )

    # Display passwords
    print("\nGenerated Password(s):\n")

    for i, password in enumerate(passwords, start=1):
        strength = check_password_strength(password)
        print(f"Password {i}: {password}")
        print(f"Strength: {strength}\n")


if __name__ == "__main__":
    main()