import tkinter as tk

def display_saying():
    root = tk.Tk()
    root.title("Favorite Saying")
    label = tk.Label(root, text="Don’t stop when you’re tired. Stop when you’re done.", font=("Helvetica", 16))
    label.pack(pady=20)
    root.mainloop()

display_saying()

# Caleb Saari 4/11/25 Wk11 Program 1: GUI Favorite Saying