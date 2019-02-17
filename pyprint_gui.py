from tkinter import *
from tkinter import ttk
import printIt as prnt


from raster_tab import Raster_Tab
from serial_settings import Serial_Settings
from text_tab import Text_Tab
from footer import Footer

def print_it():
    print("Printing")
    text_to_print = text_tab.text_entry.get("1.0", END)
    com = combo_frame.com_combobox.get()
    baud = combo_frame.baud_combobox.get()

    print(baud)
    
    if len(text_to_print) > 0:
        prnt.send_text_to_printer(text_to_print, com, baud)

def clear():
    print("Clearing Text")
    text_tab.text_entry.delete("1.0", END)

def check_coms():
        if combo_frame.active_coms:
                print(com.device for com in combo_frame.active_coms)
        else:
                footer.print_button.configure(state="disabled")

root = Tk()
root.title("PyPrint")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(False, False)

main_frame = ttk.Frame(root, padding="1 1 1 1")
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))


combo_frame = Serial_Settings(main_frame)


tabs = ttk.Notebook(main_frame)
text_tab = Text_Tab(tabs)
raster_tab = Raster_Tab(tabs)
tabs.add(text_tab, text="  Text  ")
tabs.add(raster_tab, text=" Raster ")
tabs.grid(column=0, row=1, columnspan=2, padx=10, pady=10)


footer = Footer(main_frame, print_command=print_it, clear_command=clear)


root.bind('<F1>', lambda e: print_it())

#### Main ####

check_coms()
root.mainloop()