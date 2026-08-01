# Passwords_Generator
A GUI-based Python application for generating strong and secure passwords.
# 🔐 Password Generator

A simple and customizable Password Generator built with Python. This project allows users to generate one or more secure passwords based on their preferences, such as including lowercase letters, uppercase letters, numbers, and symbols.

The project is organized using a modular structure to improve readability, maintainability, and code reusability.

---

## ✨ Features

- Generate one or multiple passwords
- Custom password length
- Include or exclude:
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Symbols
- Ensures at least one character from each selected category
- Password strength checker (Weak, Medium, Strong)
- Input validation for all user inputs
- Modular project structure

---

## 📂 Project Structure

```text
password-generator/
│
├── main.py          # Program entry point
├── generator.py     # Password generation and strength checking
├── utils.py         # User input and validation
├── README.md

```

---

## 🛠️ Technologies Used

- Python 3
- random
- string

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/sayani-code/password-generator.git
```

2. Navigate to the project folder

```bash
cd password-generator
```

3. Run the program

```bash
python main.py
```

---

## 💻 Example Output

```text
===== Password Generator =====

How many passwords do you want to generate? 2

Enter password length: 12

Include lowercase? (yes/no): yes
Include uppercase? (yes/no): yes
Include numbers? (yes/no): yes
Include symbols? (yes/no): yes

Generated Password(s):

Password 1: aT8!Lm#2Qp@R
Strength: Strong 💪

Password 2: Q9@LmX2#pRs!
Strength: Strong 💪
```

---

## 📖 What I Learned

- Python functions
- Modular programming
- Code organization
- Input validation
- Random password generation
- Working with Python's `random` and `string` modules

---

## 🚀 Future Improvements

- GUI version using Tkinter
- Copy password to clipboard
- Save generated passwords to a file
- Password history
- Generate memorable passwords
- Export passwords to CSV

---

## 👨‍💻 Author

**Sayani Saha**

GitHub: https://github.com/your-github-username