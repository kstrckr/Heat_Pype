import tkinter as tk
from tkinter import ttk

import serial as serlib

#region methods
def print_text():
    print(com_string.get())

def send_text_to_printer():
    text = text_box.get("1.0", tk.END)
    with serlib.Serial(port=com_string.get(), dsrdtr=True, baudrate=baud_rate.get()) as ser:
        ser.write(text.encode())
        ser.write(b"\x1B\x64\x0A")
        ser.write(b"\x1D\x56\x00")
#endregion

# region root and main frame
root = tk.Tk()
com_string = tk.StringVar()
baud_rate = tk.StringVar()

main_frame = ttk.Frame(root, padding="1 1 1 1")

main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)

main_frame.grid()
#endregion

#region settings label
settings_label = ttk.Label(main_frame, text="Settings:")
settings_label.grid(column=0, row=0, padx=5, pady=5, sticky=(tk.W, tk.N, tk.E, tk.S))
#endregion

#region com label
com_label = ttk.Label(main_frame, text="COM Port")
com_label.grid(column=0, row=1)

com_entry = ttk.Entry(main_frame, textvariable=com_string)
com_entry.grid(column=1, row=1, sticky=(tk.W))
#endreg

#baud label
baud_label = ttk.Label(main_frame, text="Baud Rate")
baud_label.grid(column=0, row=2)
baud_entry = ttk.Entry(main_frame, textvariable=baud_rate)
baud_entry.grid(column=1, row=2, sticky=(tk.W))
#endregion

#region text box
text_box = tk.Text(main_frame, width=48, height=20)
text_box.grid(column=0, row=3, columnspan=2)
#endregion 

#region print button
print_button = ttk.Button(main_frame, text="Print", command=send_text_to_printer)
print_button.grid(column=0, row=4, columnspan=2, sticky=(tk.W, tk.E))
#endregion

#region global padding configuration
for child in main_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)
#endregion

root.mainloop()