import tkinter as tk
import ttkbootstrap as ttk

# functions
def convert():

   feet_input = entry_str.get()
   feet_input = list(feet_input.split("'"))
   foot = float(feet_input[0])
   totalInFeet = foot
   if len(feet_input) > 1:
      inches = float(feet_input[1]) * .083
      totalInFeet += inches
   match selected_option.get():
      case "Select a measurement":
         output_string.set("Select a measurement first!")
      case "Inches":
         totalInInches = round(totalInFeet * 12, 3)
         output_string.set(str(totalInInches))
      case "Centimeters":
         totalInCentimeters = round(totalInFeet * 12 * 2.54, 3)
         output_string.set(str(totalInCentimeters))
      case "Milimeters":
         totalInMilimeters = round(totalInFeet * 12 * 2.54 * 10, 3)
         output_string.set(str(totalInMilimeters))
      case "All":
         totalInInches = round(totalInFeet * 12, 3)
         totalInCentimeters = round(totalInInches * 2.54, 3)
         totalInMilimeters = round(totalInCentimeters * 10, 3)
         allMeasurements = f'Inches: {totalInInches}\nCentimeters: {totalInCentimeters}\nMilimeters: {totalInMilimeters}'
         output_string.set(allMeasurements)



# window
window = ttk.Window(themename="vapor")
window.title("yap")
window.geometry("300x300")


# title
title_label = ttk.Label(master=window,
                       text="Feet To Units",
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

# Dropdown
selected_option = tk.StringVar()
options = ["Inches", "Centimeters", "Milimeters", "All"]
dropdown = ttk.OptionMenu(window, # master
                          selected_option, # variable
                          "Select a measurement",
                          *options)
dropdown.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window,
                        text="Output",
                        font="Calibri 24 italic",
                        textvariable=output_string)
output_label.pack(pady=5)


# run
window.mainloop()