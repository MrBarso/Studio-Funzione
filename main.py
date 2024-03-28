#in this file I combine every other file in order to do a complete study and graph of the function
import customtkinter
import tkinter
import time


#setting up graphic interface

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("900x630")

# configure grid layout (4x4)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=0)
root.grid_rowconfigure((0, 1, 2), weight=1)



#input of the function

#actual input method
def input():
    time.sleep(1)
    frame_input.destroy()

    # create sidebar frame with widgets
    root.sidebar_frame = customtkinter.CTkFrame(root, width=170, corner_radius=0)
    root.sidebar_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")
    root.sidebar_frame.grid_rowconfigure(4, weight=1)

#graphic elements
frame_input = customtkinter.CTkFrame(master=root)
frame_input.grid(pady = 15, padx = 24, row=0, column=1)

instruction = customtkinter.CTkLabel(master=frame_input, text="Enter your function!")
instruction.grid(pady = 8, padx = 5, row = 0, column = 1)

label= customtkinter.CTkLabel(master=frame_input, text="f(x) = ")
label.grid(column = 0, row = 1)

entry = customtkinter.CTkEntry(master = frame_input)
entry.grid(column = 1, row = 1, pady = 8, padx = 5)

button = customtkinter.CTkButton(master = frame_input, text="Submit function", command=input)
button.grid(pady = 8, padx = 5, row = 2, column = 1)



#start the code
root.mainloop()