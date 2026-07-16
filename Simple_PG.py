import random
import string

print("===== Password Generator =====")

# Number of passwords
count = int(input("How many passwords do you want to generate? "))

# Password length
while True:
    length = int(input("Enter password length: "))
    if length >= 4:
        break
    print("Password length must be at least 4!")

# User choices
while True :
    lower = input("Include lowercase? (yes/no): ").lower()
    upper = input("Include uppercase? (yes/no): ").lower()
    numbers = input("Include numbers? (yes/no): ").lower()
    symbols = input("Include symbols? (yes/no): ").lower()
    
    # Error if nothing is selected
    if lower in ("n","no") and upper in ("n","no") and numbers in ("n","no") and symbols in ("n","no"):
        print("Error! Select at least one character type.")
    if any(choice not in ("y", "yes", "n", "no")
       for choice in (lower, upper, numbers, symbols)):
        print("Invalid input! Please enter only y, yes, n or no.")
    else:
        break

all_characters = ""
required = []

if lower in ("y","yes"):
    all_characters += string.ascii_lowercase
    required.append(random.choice(string.ascii_lowercase))

if upper in ("y","yes"):
    all_characters += string.ascii_uppercase
    required.append(random.choice(string.ascii_uppercase))

if numbers in ("y","yes"):
    all_characters += string.digits
    required.append(random.choice(string.digits))

if symbols in ("y","yes"):
    all_characters += string.punctuation
    required.append(random.choice(string.punctuation))

print("\nGenerated Passwords:\n")

for i in range(count):
    password = required.copy()

    while len(password) < length:
        password.append(random.choice(all_characters))

    random.shuffle(password)

    print(f"Password {i+1}: {''.join(password)}")

