import tkinter as tk
import ttkbootstrap as ttk

# functions
def convert():
   feet_input = entry_str.get()
   feet_input = (list(feet_input.split("'")))
   foot = float(feet_input[0])
   inches = float(feet_input[1]) * .083
   totalInFeet = foot + inches
   totalInCentimeters = str(totalInFeet * 12 * 2.54)
   output_string.set(totalInCentimeters)

# window
window = ttk.Window(themename="vapor")
window.title("yap")
window.geometry("250x250")


# title
title_label = ttk.Label(master=window,
                       text="Feet to centimeters",
                       font="Calibri 24 bold")
title_label.pack()


# input field
input_frame = ttk.Frame(master=window)
entry_str = tk.StringVar()
entry = ttk.Entry(master=input_frame,
                 textvariable=entry_str)
button = ttk.Button(master=input_frame,
                   text="Convert",
                   command=convert)
entry.pack(side="left", padx=10)
button.pack(side="left")
input_frame.pack(pady=10)


# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window,
                        text="Output",
                        font="Calibri 24 italic",
                        textvariable=output_string)
output_label.pack(pady=5)


# run
window.mainloop()

