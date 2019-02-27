import tkinter as tk
from tkinter import ttk

def show_old_button_style():
    oldButton.grid()

root = tk.Tk()
mainFrame = ttk.Frame()
label = ttk.Label(mainFrame, text="Hello World")
helloButton = ttk.Button(mainFrame, text="Click Me")
oldButton = tk.Button(mainFrame, text="Old School")

mainFrame.grid()
label.grid()
helloButton.grid()

root.mainloop()