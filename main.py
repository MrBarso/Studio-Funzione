import customtkinter
import tkinter
import time
import control as ct
import numpy as np
import matplotlib.pyplot as plt
import math


#setting up graphic interface

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("900x630")

# configure grid layout (4x4)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=0)
root.grid_rowconfigure((0, 1, 2), weight=1)

function = "0"


#layout of the final part
def layout(function):
    
    # create sidebar frame (for the part after the function input)
    sidebar_frame = customtkinter.CTkFrame(master = root, width=170, corner_radius=0)
    sidebar_frame.grid(row=0, column=0, rowspan=20, sticky="nsew")
    sidebar_frame.grid_rowconfigure(4, weight=1)
    
    #intro label
    intro_label = customtkinter.CTkLabel(master = sidebar_frame, text = "FUNCTION EQUATION", text_color = "#1ED4B3")
    intro_label.grid(pady=10, padx=10, column=0)

    #label of the function
    function_label = customtkinter.CTkLabel(master = sidebar_frame, text = "f(x) = " + function, text_color = "#1ED4B3")
    function_label.grid(pady=2, padx=10, column=0)




#input of the function

#actual input method
def input():
    time.sleep(1)

    function = entry.get()
    

    frame_input.destroy()
    layout(function)

    

#graphic elements for the input
frame_input = customtkinter.CTkFrame(master=root)
frame_input.grid(pady = 15, padx = 24, row=0, column=1)

instruction = customtkinter.CTkLabel(master=frame_input, text="Enter your function!")
instruction.grid(pady = 8, padx = 5, row = 0, column = 1)

label= customtkinter.CTkLabel(master=frame_input, text="f(x) = ")
label.grid(column = 0, row = 1)

entry = customtkinter.CTkEntry(master = frame_input)
entry.grid(column = 1, row = 1, pady = 8, padx = 5)

button = customtkinter.CTkButton(master = frame_input, text="Submit function", hover_color='#1b89e4', command=input)
button.grid(pady = 8, padx = 5, row = 2, column = 1)



#start the code
root.mainloop()
