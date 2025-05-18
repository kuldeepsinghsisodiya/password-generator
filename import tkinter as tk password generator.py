import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be positive.")

        # Include letters, digits, and punctuation
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

# Function to copy password to clipboard
def copy_to_clipboard():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

# UI Elements
tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=5)
entry_length = tk.Entry(root, font=("Arial", 12), width=10, justify='center')
entry_length.pack(pady=5)

tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password).pack(pady=5)
entry_password = tk.Entry(root, font=("Arial", 12), width=30, justify='center')
entry_password.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), command=copy_to_clipboard).pack(pady=5)

# Start the GUI
root.mainloop()
