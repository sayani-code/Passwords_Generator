# utils.py

def get_password_count():
    
    while True:
        try:
            count = int(input("How many passwords do you want to generate? "))
            if count > 0:
                return count
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")


def get_password_length():
   
    while True:
        try:
            length = int(input("Enter password length: "))
            if length >= 4:
                return length
            print("Password length must be at least 4!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")


def get_user_choices():
    
    valid_choices = ("y", "yes", "n", "no")

    while True:
        lower = input("Include lowercase? (yes/no): ").strip().lower()
        upper = input("Include uppercase? (yes/no): ").strip().lower()
        numbers = input("Include numbers? (yes/no): ").strip().lower()
        symbols = input("Include symbols? (yes/no): ").strip().lower()

        # Check for invalid input
        if any(choice not in valid_choices
               for choice in (lower, upper, numbers, symbols)):
            print("Invalid input! Please enter only y, yes, n or no.\n")
            continue

        # At least one option must be selected
        if all(choice in ("n", "no")
               for choice in (lower, upper, numbers, symbols)):
            print("Error! Select at least one character type.\n")
            continue

        return lower, upper, numbers, symbols