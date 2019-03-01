import tkinter as tk
from tkinter import ttk

def show_old_button_style():
    oldButton.grid()

def delete_old_button():
    oldButton.forget()

root = tk.Tk()

mainFrame = ttk.Frame(root, padding="5 5 5 5")

label = ttk.Label(mainFrame, anchor="center", text="Hello World")

helloButton = ttk.Button(mainFrame, text="ttk Themed", command=show_old_button_style)

oldButton = tk.Button(mainFrame, text="Non-Themed")

#--------------------------------------------------

mainFrame.grid()

label.grid(sticky=(tk.W, tk.E))

helloButton.grid(sticky="nsew")

root.mainloop()