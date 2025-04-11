# GUI Program to Display Name and Address

import tkinter as tk
from tkinter import messagebox

def show_info():
    messagebox.showinfo("Information", "Name: Caleb Saari\nAddress: 6853 256th St, Wyoming, MN 55092, USA")

def quit_app():
    root.quit()

root = tk.Tk()
root.title("Info Display")

show_info_button = tk.Button(root, text="Show Info", command=show_info)
show_info_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.pack(pady=10)

root.mainloop()
