import tkinter as tk
from tkinter import ttk
from pyprint.printIt import EpsonCommands as Eps

from pyprint.menubars import PyPrintMenus
from pyprint.serialsettings import Serial_Settings
from pyprint.printingtabs import Printing_Tabs
from pyprint.footer import Footer

def print_it():
    print("Printing")
    text_to_print = tabs.Get_Text_Input()
    com = combo_frame.com_combobox.get()
    baud = combo_frame.baud_combobox.get()

    print(baud)
    
    if len(text_to_print) > 0:
        Eps.send_text_to_printer(text_to_print, com, baud)

def clear():
    print("Clearing Text")
    tabs.Clear_Text()

def check_coms():
        if combo_frame.active_coms:
                print(com.device for com in combo_frame.active_coms)
        else:
                action_buttons.print_button.configure(state="disabled")

root = tk.Tk()
root.option_add('*tearOff', tk.FALSE)


root.title("PyPrint")
root.columnconfigure(0, weight=1)
root.resizable(False, False)

menubar = PyPrintMenus(root)
root.config(menu=menubar)


main_frame = ttk.Frame(root, padding="1 1 1 1")
main_frame.columnconfigure(0, weight=0)
main_frame.columnconfigure(1, weight=1)
main_frame.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.S, tk.W))


combo_frame = Serial_Settings(main_frame, column=0, row=0,  sticky=(tk.W), padx=10)
action_buttons = Footer(main_frame, column=1, row=0, sticky=(tk.N, tk.E, tk.S, tk.W), padx=10)
action_buttons.bind_buttons(print_it, clear)
tabs = Printing_Tabs(main_frame, column=0, row=1, columnspan=2, padx=10, pady=10)


root.bind('<F1>', lambda e: print_it())

#### Main ####

check_coms()
root.mainloop()