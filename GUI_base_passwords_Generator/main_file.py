import tkinter as tk

from gui_file import PasswordGeneratorApp


def main():

    root = tk.Tk()

    PasswordGeneratorApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()