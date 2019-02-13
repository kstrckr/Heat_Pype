from tkinter import *
from tkinter import ttk
from printIt import *

#global UI vars
# available_coms = return_active_coms()
available_coms = return_active_coms()
print(available_coms[0].device)

def print_it():
    text_to_print=text_entry.get("1.0", END)
    com = com_combobox.get()
    baud = baud_combobox.get()
    
    if len(text_to_print) > 0:
        send_text_to_printer(text_to_print, com, baud)

def clear():
    text_entry.delete("1.0", END)

root = Tk()
root.title("PyPrint")
selected_coms = StringVar(root)
selected_baud = IntVar(root)

main_frame = ttk.Frame(root, padding="1 1 1 1")
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(False, False)

combo_frame = ttk.Frame(main_frame)
combo_frame.grid(column=0, row=0, columnspan=2, sticky=(W, E), padx=10)
ttk.Label(combo_frame, text="Serial Settings:").grid(column=0, row=0, sticky=(W, E), pady=5)

com_combobox = ttk.Combobox(combo_frame, textvariable=selected_coms, values=[com.device for com in available_coms], state="readonly")
com_combobox.grid(column=1, row=1, sticky=(W, E))
com_combobox.set(available_coms[0].device)
ttk.Label(combo_frame, text="COM Port").grid(column=0, row=1, sticky=(W))

ttk.Separator(combo_frame, orient=HORIZONTAL).grid(column=1, row=2, sticky=(W, E))

baud_combobox = ttk.Combobox(combo_frame, textvariable=selected_baud, values=Baud.rates, state="readonly")
baud_combobox.grid(column=1, row=3, sticky=(W, E))
baud_combobox.set(38400)
ttk.Label(combo_frame, text="Baud Rate").grid(column=0, row=3, sticky=(W))

text_entry = Text(main_frame, width=48, height=10)
text_entry.grid(column=0, row=1, columnspan=2, sticky=(N, W), padx=10, pady=10)

ttk.Button(main_frame, text="Print", command=print_it).grid(column=0, row=2, sticky=(W, E), padx=10, pady=10)
ttk.Button(main_frame, text="Clear", command=clear).grid(column=1, row=2, sticky=(W, E), padx=10, pady=10)

root.bind('<F1>', lambda e: print_it())
#### Main Loop ####

root.mainloop()