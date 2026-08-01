import tkinter as tk
from tkinter import messagebox

from generator_file import generate_passwords, check_password_strength


class PasswordGeneratorApp:

    def __init__(self, root):

        self.root = root

        # -----------------------------
        # Window settings
        # -----------------------------

        self.root.title("Password Generator Application")
        self.root.geometry("650x650")
        self.root.resizable(False, False)

        self.root.configure(bg="#f2f2f2")

        # Store generated password
        self.generated_password = ""

        # -----------------------------
        # Tkinter variables
        # -----------------------------

        self.upper_var = tk.StringVar(value="yes")
        self.lower_var = tk.StringVar(value="yes")
        self.number_var = tk.StringVar(value="yes")
        self.symbol_var = tk.StringVar(value="yes")

        # -----------------------------
        # Title
        # -----------------------------

        title_label = tk.Label(
            root,
            text="Password Generator Application",
            font=("Arial", 22, "bold"),
            bg="#f2f2f2"
        )

        title_label.pack(pady=25)

        # -----------------------------
        # Main frame
        # -----------------------------

        main_frame = tk.Frame(
            root,
            bg="#f2f2f2"
        )

        main_frame.pack(pady=10)

        # -----------------------------
        # Password Length
        # -----------------------------

        length_label = tk.Label(
            main_frame,
            text="Password Length",
            font=("Arial", 13),
            bg="#f2f2f2"
        )

        length_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=15,
            pady=12
        )

        self.length_entry = tk.Entry(
            main_frame,
            width=15,
            font=("Arial", 13)
        )

        self.length_entry.grid(
            row=0,
            column=1,
            columnspan=2,
            padx=10,
            pady=12
        )

        # -----------------------------
        # Uppercase
        # -----------------------------

        uppercase_label = tk.Label(
            main_frame,
            text="Include Uppercase Letters",
            font=("Arial", 13),
            bg="#f2f2f2"
        )

        uppercase_label.grid(
            row=1,
            column=0,
            sticky="w",
            padx=15,
            pady=10
        )

        self.create_yes_no_buttons(
            main_frame,
            self.upper_var,
            row=1
        )

        # -----------------------------
        # Lowercase
        # -----------------------------

        lowercase_label = tk.Label(
            main_frame,
            text="Include Lowercase Letters",
            font=("Arial", 13),
            bg="#f2f2f2"
        )

        lowercase_label.grid(
            row=2,
            column=0,
            sticky="w",
            padx=15,
            pady=10
        )

        self.create_yes_no_buttons(
            main_frame,
            self.lower_var,
            row=2
        )

        # -----------------------------
        # Numbers
        # -----------------------------

        numbers_label = tk.Label(
            main_frame,
            text="Include Numbers",
            font=("Arial", 13),
            bg="#f2f2f2"
        )

        numbers_label.grid(
            row=3,
            column=0,
            sticky="w",
            padx=15,
            pady=10
        )

        self.create_yes_no_buttons(
            main_frame,
            self.number_var,
            row=3
        )

        # -----------------------------
        # Symbols
        # -----------------------------

        symbols_label = tk.Label(
            main_frame,
            text="Include Special Symbols",
            font=("Arial", 13),
            bg="#f2f2f2"
        )

        symbols_label.grid(
            row=4,
            column=0,
            sticky="w",
            padx=15,
            pady=10
        )

        self.create_yes_no_buttons(
            main_frame,
            self.symbol_var,
            row=4
        )

        # -----------------------------
        # Generate Button
        # -----------------------------

        generate_button = tk.Button(
            root,
            text="GENERATE PASSWORD",
            font=("Arial", 13, "bold"),
            bg="#2196F3",
            fg="white",
            width=25,
            command=self.generate_password
        )

        generate_button.pack(pady=25)

        # -----------------------------
        # Password output
        # -----------------------------

        self.password_entry = tk.Entry(
            root,
            font=("Consolas", 15),
            width=35,
            justify="center",
            state="readonly"
        )

        self.password_entry.pack(pady=10)

        # -----------------------------
        # Strength Label
        # -----------------------------

        self.strength_label = tk.Label(
            root,
            text="",
            font=("Arial", 12, "bold"),
            bg="#f2f2f2"
        )

        self.strength_label.pack(pady=5)

        # -----------------------------
        # Accept Button
        # -----------------------------

        accept_button = tk.Button(
            root,
            text="ACCEPT",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            width=12,
            command=self.accept_password
        )

        accept_button.pack(pady=10)

        # -----------------------------
        # Reset Button
        # -----------------------------

        reset_button = tk.Button(
            root,
            text="RESET",
            font=("Arial", 12, "bold"),
            bg="#F44336",
            fg="white",
            width=12,
            command=self.reset_form
        )

        reset_button.pack(pady=5)

    # =====================================================
    # Create Yes / No buttons
    # =====================================================

    def create_yes_no_buttons(self, parent, variable, row):

        yes_button = tk.Radiobutton(
            parent,
            text="YES",
            variable=variable,
            value="yes",
            indicatoron=False,
            width=7,
            bg="#4CAF50",
            fg="white",
            selectcolor="#2E7D32",
            font=("Arial", 10, "bold")
        )

        yes_button.grid(
            row=row,
            column=1,
            padx=8,
            pady=5
        )

        no_button = tk.Radiobutton(
            parent,
            text="NO",
            variable=variable,
            value="no",
            indicatoron=False,
            width=7,
            bg="#F44336",
            fg="white",
            selectcolor="#C62828",
            font=("Arial", 10, "bold")
        )

        no_button.grid(
            row=row,
            column=2,
            padx=8,
            pady=5
        )

    # =====================================================
    # Generate Password
    # =====================================================

    def generate_password(self):

        try:

            # Get password length
            length_text = self.length_entry.get().strip()

            if not length_text:
                messagebox.showerror(
                    "Error",
                    "Please enter a password length."
                )
                return

            length = int(length_text)

            if length < 4:
                messagebox.showerror(
                    "Error",
                    "Password length must be at least 4."
                )
                return

            # Convert Yes/No into Boolean values
            upper = self.upper_var.get() == "yes"
            lower = self.lower_var.get() == "yes"
            numbers = self.number_var.get() == "yes"
            symbols = self.symbol_var.get() == "yes"

            # Check that something is selected
            if not any([
                upper,
                lower,
                numbers,
                symbols
            ]):
                messagebox.showerror(
                    "Error",
                    "Please select at least one character type."
                )
                return

            # We only need one password for this GUI
            passwords = generate_passwords(
                count=1,
                length=length,
                lower=lower,
                upper=upper,
                numbers=numbers,
                symbols=symbols
            )

            self.generated_password = passwords[0]

            # Display password
            self.password_entry.config(
                state="normal"
            )

            self.password_entry.delete(
                0,
                tk.END
            )

            self.password_entry.insert(
                0,
                self.generated_password
            )

            self.password_entry.config(
                state="readonly"
            )

            # Check strength
            strength = check_password_strength(
                self.generated_password
            )

            self.show_strength(strength)

        except ValueError as error:

            messagebox.showerror(
                "Invalid Input",
                str(error)
            )

    # =====================================================
    # Show Password Strength
    # =====================================================

    def show_strength(self, strength):

        if strength == "Strong":

            self.strength_label.config(
                text="Strength: Strong",
                fg="green"
            )

        elif strength == "Medium":

            self.strength_label.config(
                text="Strength: Medium",
                fg="orange"
            )

        else:

            self.strength_label.config(
                text="Strength: Weak",
                fg="red"
            )

    # =====================================================
    # Accept Password
    # =====================================================

    def accept_password(self):

        if not self.generated_password:

            messagebox.showwarning(
                "No Password",
                "Please generate a password first."
            )

            return

        # Copy password to clipboard
        self.root.clipboard_clear()

        self.root.clipboard_append(
            self.generated_password
        )

        self.root.update()

        messagebox.showinfo(
            "Password Accepted",
            "Password copied to clipboard!"
        )

    # =====================================================
    # Reset
    # =====================================================

    def reset_form(self):

        # Clear length
        self.length_entry.delete(
            0,
            tk.END
        )

        # Reset options
        self.upper_var.set("yes")
        self.lower_var.set("yes")
        self.number_var.set("yes")
        self.symbol_var.set("yes")

        # Remove generated password
        self.generated_password = ""

        self.password_entry.config(
            state="normal"
        )

        self.password_entry.delete(
            0,
            tk.END
        )

        self.password_entry.config(
            state="readonly"
        )

        # Clear strength
        self.strength_label.config(
            text=""
        )