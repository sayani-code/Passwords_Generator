import random
import string

print("===== Password Generator =====")

# Ask for password length
length = int(input("Enter password length(minimum 4): "))

# Ask what to include
lower = input("Include lowercase letters? (yes/no): ").lower()
upper = input("Include uppercase letters? (yes/no): ").lower()
numbers = input("Include numbers? (yes/no): ").lower()
symbols = input("Include symbols? (yes/no): ").lower()

# Create an empty string to store all allowed characters
characters = ""

# Add character groups based on user choice
if lower in ("y","yes"):
    characters += string.ascii_lowercase

if upper in ("y","yes"):
    characters += string.ascii_uppercase

if numbers in ("y","yes"):
    characters += string.digits

if symbols in ("y","yes"):
    characters += string.punctuation

# Check if at least one option was selected
if characters == "":
    print("Error: You must choose at least one character type.")
else:
    password = ""

    # Generate password
    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)