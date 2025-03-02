import itertools
import string
import tkinter as tk
from tkinter import messagebox
import os

# Hardcoded password (must be 5 alphabetical characters)
CORRECT_PASSWORD = "Hello"

# Dictionary file path
DICTIONARY_FILE = "rockyou.txt"  # Ensure this file is in the same directory

def load_dictionary(file_path):
    """Load passwords from a dictionary file, handling encoding issues."""
    if not os.path.exists(file_path):
        messagebox.showerror("Error", f"Dictionary file '{file_path}' not found.")
        return []    
    try:
        with open(file_path, "r", encoding="latin-1") as file:  # Use latin-1 to avoid Unicode errors
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read dictionary file: {str(e)}")
        return []

def dictionary_attack(dictionary):
    """Attempt to crack the password using a dictionary attack."""
    for password in dictionary:
        if password == CORRECT_PASSWORD:
            return f"Dictionary attack succeeded. Password found: {password}"
    return "Dictionary attack failed."

def brute_force_attack():
    """Attempt to crack the password using a brute force attack."""
    chars = string.ascii_letters  # a-z followed by A-Z
    for count, candidate in enumerate(itertools.product(chars, repeat=5), start=1):
        candidate = ''.join(candidate)
        if candidate == CORRECT_PASSWORD:
            return f"Brute force attack succeeded. Password found: {candidate}\nTotal attempts: {count}"
    return "Brute force attack failed."

def start_attack():
    username = username_entry.get()
    dictionary = load_dictionary(DICTIONARY_FILE)
    result = dictionary_attack(dictionary)
    if "failed" in result:
        result = brute_force_attack()
    
    messagebox.showinfo("Attack Result", f"User: {username}\n{result}")

# GUI Setup
root = tk.Tk()
root.title("Password Cracker")
root.geometry("400x250")

tk.Label(root, text="Enter Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Button(root, text="Start Attack", command=start_attack).pack(pady=20)

tk.Label(root, text="Ensure 'rockyou.txt' is in the same folder.", fg="red").pack(pady=5)

root.mainloop()