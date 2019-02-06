from tkinter import *
from tkinter import ttk
from printIt import send_text_to_printer

def print_it():
    text_to_print=text_entry.get("1.0", END)
    
    if len(text_to_print) > 0:
        send_text_to_printer(text_to_print)


def clear():
    text_entry.delete("1.0", END)

root = Tk()
root.title("PyPrint")

main_frame = ttk.Frame(root, padding="1 1 1 1")
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

text_entry = Text(main_frame, width=48, height=10)
text_entry.grid(column=0, row=0, sticky=(N, W), padx=10, pady=10)

ttk.Button(main_frame, text="Print", command=print_it).grid(column=0, row=2, sticky=(W, E), padx=10, pady=10)
ttk.Button(main_frame, text="Clear", command=clear).grid(column=0, row=3, sticky=(W, E), padx=10, pady=10)

root.bind('<F1>', lambda e: print_it())
#### Main Loop ####

root.mainloop()