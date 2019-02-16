from tkinter import *
from tkinter import ttk
from printIt import *


from raster_tab import Raster_Tab
from serial_settings import Serial_Settings
from text_tab import Text_Tab
from footer import Footer

# available_coms = return_active_coms()

#region Global UI Functions
def print_it():
    text_to_print=text_tab.text_entry.get("1.0", END)
    com = com_combobox.get()
    baud = baud_combobox.get()
    
    if len(text_to_print) > 0:
        send_text_to_printer(text_to_print, com, baud)

def clear():
    print("Clearing Text")
    text_tab.text_entry.delete("1.0", END)

def populate_com_combobox():
        if available_coms:
                com_combobox.set(available_coms[0].device)
                print(available_coms[0].device)
        else:
                com_combobox.set("No Coms Detected")
                baud_combobox.set("0")
                com_combobox.configure(state="disabled")
                baud_combobox.configure(state="disabled")
                footer.print_button.configure(state="disabled")
#endregion

#region Root Instantiation
root = Tk()
root.title("PyPrint")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(False, False)
#endregion

#region Global Var Bindings
selected_coms = StringVar()
selected_baud = IntVar()
#endregion

#region Main Frame
main_frame = ttk.Frame(root, padding="1 1 1 1")
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

#region Combobox Frame
combo_frame = Serial_Settings(main_frame)
combo_frame.grid(column=0, row=0, columnspan=2, sticky=(W, E), padx=10)




com_combobox = ttk.Combobox(combo_frame, textvariable=selected_coms, values=[com.device for com in available_coms], state="readonly")
com_combobox.grid(column=1, row=1, sticky=(W, E))
ttk.Label(combo_frame, text="COM Port").grid(column=0, row=1, sticky=(W))

ttk.Separator(combo_frame, orient=HORIZONTAL).grid(column=1, row=2, sticky=(W, E))

baud_combobox = ttk.Combobox(combo_frame, textvariable=selected_baud, values=Baud.rates, state="readonly")
baud_combobox.grid(column=1, row=3, sticky=(W, E))
baud_combobox.set(38400)
ttk.Label(combo_frame, text="Baud Rate").grid(column=0, row=3, sticky=(W))
#endregion

tabs = ttk.Notebook(main_frame)
text_tab = Text_Tab(tabs)
raster_tab = Raster_Tab(tabs)
tabs.add(text_tab, text="  Text  ")
tabs.add(raster_tab, text=" Raster ")
tabs.grid(column=0, row=1, columnspan=2, padx=10, pady=10)


footer = Footer(main_frame, print_command=print_it, clear_command=clear)


#region Keyboard Shotcut Bindings
root.bind('<F1>', lambda e: print_it())
#endregion

#### Main ####

populate_com_combobox()
root.mainloop()