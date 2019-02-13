from tkinter import *
from tkinter import ttk
from printIt import *

available_coms = return_active_coms()

#region Global UI Functions
def print_it():
    text_to_print=text_entry.get("1.0", END)
    com = com_combobox.get()
    baud = baud_combobox.get()
    
    if len(text_to_print) > 0:
        send_text_to_printer(text_to_print, com, baud)

def clear():
    text_entry.delete("1.0", END)

def populate_com_combobox():
        if available_coms:
                com_combobox.set(available_coms[0].device)
                print(available_coms[0].device)
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
combo_frame = ttk.Frame(main_frame)
combo_frame.grid(column=0, row=0, columnspan=2, sticky=(W, E), padx=10)
ttk.Label(combo_frame, text="Serial Settings:").grid(column=0, row=0, sticky=(W, E), pady=5)

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

#region Text Entry
text_tab_frame = ttk.Frame(tabs)
tabs.add(text_tab_frame, text="Text")
text_entry = Text(text_tab_frame, width=48, height=10)
text_entry.grid(column=0, row=0, sticky=(N, W), padx=10, pady=10)
#endregion

raster_tab_frame = ttk.Frame(tabs)
tabs.add(raster_tab_frame, text="Raster")
raster_canvas = Canvas(raster_tab_frame, width=475, height=206)
imgobj = PhotoImage(file='monobmp.gif')


print()

raster_canvas.create_image(0, 0, image=imgobj, anchor=NW)
raster_canvas.grid(column=0, row=0, sticky=(N,E,S,W), padx=10, pady=10)

tabs.grid(column=0, row=1, columnspan=2, sticky=(N, W), padx=10, pady=10)

#region Print Buttons
print_button = ttk.Button(main_frame, text="Print", command=print_it)
print_button.grid(column=0, row=2, sticky=(W, E), padx=10, pady=10)

clear_button = ttk.Button(main_frame, text="Clear", command=clear)
clear_button.grid(column=1, row=2, sticky=(W, E), padx=10, pady=10)
#endregion

#endregion

#region Keyboard Shotcut Bindings
root.bind('<F1>', lambda e: print_it())
#endregion

#### Main ####

populate_com_combobox()
root.mainloop()