import tkinter as tk
from tkinter import ttk

def move_line(value=None):
    int_x = slider_x.get()
    int_y = slider_y.get()
    can.delete("line_1")
    can.create_line((250,250,int_x,int_y), width=2, fill="black", tags="line_1")

def open_settings(target_canvas):
    settings_win = tk.Tk()
    settings_frame = ttk.Frame(settings_win, padding="5 5 5 5")
    settings_frame.pack()

    color_label = ttk.Label(settings_frame, text="Circle Color")
    color_label.pack(side="left")
    color_combobox = ttk.Combobox(settings_frame, values=["red", "green", "blue"], state="readonly")
    color_combobox.set("red")
    color_combobox.pack()

    button_frame = ttk.Frame(settings_win, padding="5 5 5 5")
    button_frame.pack()

    apply_button = ttk.Button(button_frame, text="Save", command=lambda: set_circle_color(color_combobox.get(), settings_win, target_canvas))
    apply_button.pack()

def set_circle_color(color, settings_window, canvas):
    canvas.delete("circle")
    canvas.create_oval((25, 25, 475, 475), dash=1, width=3, outline=color, tags="circle")
    settings_window.destroy()

class Menu_Bar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        parent['menu'] = self

        menu_file = tk.Menu(self)
        menu_edit = tk.Menu(self)

        self.add_cascade(menu=menu_file, label="File")
        self.add_cascade(menu=menu_edit, label="Edit")

        menu_file.add_command(label="Quit", command=exit)
        menu_edit.add_command(label="Settings", command=lambda: open_settings(can))

root = tk.Tk()
root.resizable(False, False)

main_frame = ttk.Frame(root, padding="1 1 1 1")
main_frame.pack(side="top")

canvas_frame = ttk.Frame(main_frame, padding="1 1 1 1")
canvas_frame.pack()

can = tk.Canvas(canvas_frame, bg="gray", height=500, width=500)
can.create_oval((25, 25, 475, 475), dash=1, width=3, outline="red", tags="circle")
can.pack(side="right")

slider_y = ttk.Scale(canvas_frame, from_=0, to=500, length=500, orient="vertical", command=move_line)
slider_y.pack()

interface_frame = ttk.Frame(main_frame, padding="1 1 1 1")
interface_frame.pack()

slider_x = ttk.Scale(interface_frame, from_=0, to=500, length=500, command=move_line)
slider_x.pack(anchor="w")


root.option_add('*tearOff', tk.FALSE)
root.bind("<Control-q>", exit)
menu = Menu_Bar(root)
move_line()
root.mainloop()