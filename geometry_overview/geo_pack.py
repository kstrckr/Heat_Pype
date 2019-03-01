import tkinter as tk
from tkinter import ttk

root = tk.Tk()

main_frame = ttk.Frame(root)
main_frame.pack(expand=1, fill="both")

#region pack frame
pack_frame = ttk.Frame(main_frame)
pack_frame.pack(expand=1, fill="both", side="left")
#endregion

#region grid_frame
# grid_frame = ttk.Frame(main_frame)
# grid_frame.rowconfigure(0, weight=1)
# grid_frame.columnconfigure(0, weight=1)
# grid_frame.pack(expand=1, fill="both", anchor="e", side="right")
#endregion

#region label one
# label_one = ttk.Label(pack_frame, text="This side's Packed", background="red")
# label_one.pack(expand=1, fill="both")
#endregion

#region label two
# label_two = ttk.Label(pack_frame, text="I'm Blue", background="blue")
# label_two.pack(expand=1, fill="both")
#end region

#region button in grid
# button = ttk.Button(grid_frame, text="I'm in a grid")
# button.grid()
#endregion

root.mainloop()