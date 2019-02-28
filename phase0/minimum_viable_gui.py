import tkinter as tk
from tkinter import ttk

def show_old_button_style():
    oldButton.grid()

root = tk.Tk()
mainFrame = ttk.Frame(root)

label = ttk.Label(mainFrame, anchor="center", text="Hello World")
helloButton = ttk.Button(mainFrame, text="Click Me")
oldButton = tk.Button(mainFrame, text="Old School")

mainFrame.grid(padx=10, pady=10, sticky=(tk.W, tk.E))
label.grid(sticky=(tk.W, tk.E))
helloButton.grid(sticky="nsew")

root.mainloop()