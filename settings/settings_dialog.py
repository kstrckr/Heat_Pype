import tkinter as tk
from tkinter import ttk

root = tk.Tk()

s = ttk.Style()
s.configure('My.TFrame', background="red")

mainFrame = ttk.Frame(root, style='My.TFrame')
mainFrame.grid()

button = ttk.Button(mainFrame, style='My.TFrame')
button.grid()

root.mainloop()