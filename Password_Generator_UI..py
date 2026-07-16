import secrets
import string
import tkinter as tk
from tkinter import messagebox


class PasswordGeneratorApp:
    

    GREEN = "#2e9d52"
    RED = "#d94b4b"
    BLUE = "#2878c8"
    DARK = "#17324d"
    LIGHT = "#f4f8fc"
    PLACEHOLDER = "Enter a number"

    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator Application")
        self.root.geometry("650x520")
        self.root.resizable(False, False)
        self.root.configure(bg=self.LIGHT)

        self.options = [
            ("Include uppercase letters", string.ascii_uppercase),
            ("Include lowercase letters", string.ascii_lowercase),
            ("Include numbers", string.digits),
            ("Include special symbols", string.punctuation),
        ]

        self.choice_vars = [tk.BooleanVar(value=True) for _ in self.options]
        self.length_var = tk.StringVar(value=self.PLACEHOLDER)
        self.password_var = tk.StringVar()
        self.status_var = tk.StringVar(
            value="Choose options, then click Accept."
        )

        # Settings saved after the Accept button is clicked.
        self.accepted_length = None
        self.accepted_sets = None
        self.option_buttons = []

        self.build_interface()

    def build_interface(self):
        """Create all GUI widgets."""

        title = tk.Label(
            self.root,
            text="Password Generator Application",
            font=("Arial", 20, "bold"),
            fg=self.DARK,
            bg=self.LIGHT,
        )
        title.pack(pady=(26, 18))

        card = tk.Frame(
            self.root,
            bg="white",
            bd=1,
            relief="solid",
            padx=28,
            pady=22,
        )
        card.pack(padx=50, fill="x")

        tk.Label(
            card,
            text="Password length",
            font=("Arial", 12, "bold"),
            bg="white",
        ).grid(row=0, column=0, sticky="w", pady=(0, 16))

        self.length_entry = tk.Entry(
            card,
            textvariable=self.length_var,
            width=14,
            font=("Arial", 12),
            justify="center",
            fg="gray",
        )
        self.length_entry.grid(row=0, column=1, sticky="e", pady=(0, 16))

        # Placeholder and saved-setting behavior for the length entry.
        self.length_entry.bind("<FocusIn>", self.remove_placeholder)
        self.length_entry.bind("<FocusOut>", self.restore_placeholder)
        self.length_entry.bind("<KeyRelease>", self.length_changed)

        for row, ((label, _characters), choice) in enumerate(
            zip(self.options, self.choice_vars),
            start=1,
        ):
            tk.Label(
                card,
                text=label,
                font=("Arial", 12),
                bg="white",
            ).grid(row=row, column=0, sticky="w", pady=6)

            buttons = tk.Frame(card, bg="white")
            buttons.grid(row=row, column=1, sticky="e", pady=6)

            yes_button = tk.Button(
                buttons,
                text="Yes",
                command=lambda index=row - 1: self.set_choice(index, True),
                bg=self.GREEN,
                activebackground=self.GREEN,
                fg="white",
                activeforeground="white",
                font=("Arial", 10, "bold"),
                width=5,
                relief=tk.SUNKEN,
                bd=3,
            )
            yes_button.pack(side="left", padx=(0, 8))

            no_button = tk.Button(
                buttons,
                text="No",
                command=lambda index=row - 1: self.set_choice(index, False),
                bg=self.RED,
                activebackground=self.RED,
                fg="white",
                activeforeground="white",
                font=("Arial", 10, "bold"),
                width=5,
                relief=tk.RAISED,
                bd=3,
            )
            no_button.pack(side="left")

            self.option_buttons.append((yes_button, no_button))

        actions = tk.Frame(self.root, bg=self.LIGHT)
        actions.pack(pady=18)

        tk.Button(
            actions,
            text="ACCEPT",
            command=self.accept_choices,
            bg=self.GREEN,
            fg="white",
            activebackground=self.GREEN,
            activeforeground="white",
            font=("Arial", 11, "bold"),
            width=11,
        ).pack(side="left", padx=8)

        tk.Button(
            actions,
            text="GENERATE PASSWORD",
            command=self.generate_password,
            bg=self.BLUE,
            fg="white",
            activebackground=self.BLUE,
            activeforeground="white",
            font=("Arial", 11, "bold"),
            width=22,
        ).pack(side="left", padx=8)

        tk.Button(
            actions,
            text="RESET",
            command=self.reset,
            bg=self.RED,
            fg="white",
            activebackground=self.RED,
            activeforeground="white",
            font=("Arial", 11, "bold"),
            width=10,
        ).pack(side="left", padx=8)

        tk.Label(
            self.root,
            text="Generated password",
            font=("Arial", 11, "bold"),
            bg=self.LIGHT,
        ).pack()

        result = tk.Entry(
            self.root,
            textvariable=self.password_var,
            font=("Consolas", 14),
            justify="center",
            width=42,
            state="readonly",
            readonlybackground="white",
            bd=2,
            relief="groove",
        )
        result.pack(pady=(6, 8), ipady=7)

        tk.Label(
            self.root,
            textvariable=self.status_var,
            font=("Arial", 10),
            fg=self.DARK,
            bg=self.LIGHT,
        ).pack()

    def selected_characters(self):
        #Return all character groups currently set to Yes.
        return [
            characters
            for (_label, characters), selected in zip(
                self.options,
                self.choice_vars,
            )
            if selected.get()
        ]

    def remove_placeholder(self, _event=None):
        
        if self.length_var.get() == self.PLACEHOLDER:
            self.length_var.set("")
            self.length_entry.configure(fg="black")

    def restore_placeholder(self, _event=None):
        
        if not self.length_var.get().strip():
            self.length_var.set(self.PLACEHOLDER)
            self.length_entry.configure(fg="gray")

    def clear_length_entry(self):
        
        self.length_var.set(self.PLACEHOLDER)
        self.length_entry.configure(fg="gray")

    def length_changed(self, _event=None):
        
        self.accepted_length = None
        self.accepted_sets = None
        self.status_var.set("Length changed. Click Accept to save it.")

    def set_choice(self, index, value):
        #Set a Yes/No option 
        self.choice_vars[index].set(value)

        yes_button, no_button = self.option_buttons[index]

        yes_button.configure(
            relief=tk.SUNKEN if value else tk.RAISED
        )
        no_button.configure(
            relief=tk.RAISED if value else tk.SUNKEN
        )

        # Changed options must be accepted again.
        self.accepted_length = None
        self.accepted_sets = None
        self.status_var.set("Choices changed. Click Accept to save them.")

    def get_length(self):
        
        entry_value = self.length_var.get().strip()

        if not entry_value or entry_value == self.PLACEHOLDER:
            messagebox.showerror(
                "Invalid length",
                "Enter a password length.",
            )
            return None

        try:
            length = int(entry_value)
        except ValueError:
            messagebox.showerror(
                "Invalid length",
                "Password length must be a whole number.",
            )
            return None

        if length < 4:
            messagebox.showerror(
                "Invalid length",
                "Password length must be at least 4.",
            )
            return None

        return length

    def accept_choices(self):
        
        length = self.get_length()

        if length is None:
            return

        character_sets = self.selected_characters()

        if not character_sets:
            messagebox.showerror(
                "No character type",
                "Select Yes for at least one character type.",
            )
            return

        self.accepted_length = length
        self.accepted_sets = character_sets

        
        self.status_var.set(
            "Choices accepted. Click Generate Password."
        )

    def generate_password(self):
        
        if self.accepted_length is None or self.accepted_sets is None:
            messagebox.showinfo(
                "Accept choices",
                "Enter a length, select options, then click Accept.",
            )
            return

        length = self.accepted_length
        character_sets = self.accepted_sets

        if length < len(character_sets):
            messagebox.showerror(
                "Invalid length",
                "Password length is too short for the selected character types.",
            )
            return

        # Include at least one character from every selected type.
        password = [
            secrets.choice(characters)
            for characters in character_sets
        ]

        all_characters = "".join(character_sets)

        password.extend(
            secrets.choice(all_characters)
            for _ in range(length - len(password))
        )

        secrets.SystemRandom().shuffle(password)

        self.password_var.set("".join(password))
        self.status_var.set("New password generated.")

    def reset(self):
        """Restore the GUI to its default state."""
        self.clear_length_entry()
        self.password_var.set("")
        self.accepted_length = None
        self.accepted_sets = None

        # Set every option back to Yes.
        for index in range(len(self.choice_vars)):
            self.set_choice(index, True)

        self.status_var.set(
            "Reset complete. Choose options, then click Accept."
        )


if __name__ == "__main__":
    root = tk.Tk()
    PasswordGeneratorApp(root)
    root.mainloop()