import tkinter as tk
from tkinter import filedialog, messagebox

def save_file(content, file_type="txt"):
    file_path = filedialog.asksaveasfilename(defaultextension=f".{file_type}",
                                             filetypes=[(f"{file_type.upper()} files", f"*.{file_type}")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(content)
        messagebox.showinfo("Success", f"File saved successfully as {file_path}")

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            return file.read()
    return ""