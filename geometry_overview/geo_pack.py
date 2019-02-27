import tkinter as tk
from tkinter import ttk

root = tk.Tk()

mainFrame = ttk.Frame(root)
mainFrame.pack(expand=1, fill="both")

label_one = ttk.Label(mainFrame, text="Red", background="red")
label_one.pack(expand=1, fill="both")

label_two = ttk.Label(mainFrame, text="Blue", background="blue")
label_two.pack(expand=1, fill="both")

root.mainloop()