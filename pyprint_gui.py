from tkinter import *
from tkinter import ttk
from printIt import *


from raster_tab import Raster_Tab
from serial_settings import Serial_Settings
from text_tab import Text_Tab
from footer import Footer

def print_it():
    print("Printing")
    # text_to_print=text_tab.text_entry.get("1.0", END)
    # com = com_combobox.get()
    # baud = baud_combobox.get()
    
    # if len(text_to_print) > 0:
    #     send_text_to_printer(text_to_print, com, baud)

def clear():
    print("Clearing Text")
    text_tab.text_entry.delete("1.0", END)

def check_coms():
        if combo_frame.active_coms:
                print(com.device for com in combo_frame.active_coms)
        else:
                footer.print_button.configure(state="disabled")


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

# populate_com_combobox()
check_coms()
root.mainloop()