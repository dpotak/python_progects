from tkinter import *
from tkinter import Tk
from tkinter import Button
from tkinter import Label

def open_folder():
    pass

# Start programs
root = Tk()

# Setting programm
root.title("Glasses")
root.geometry("450x450")
root.resizable(True, True)

# Button for open folder 
btn_open_folder = Button(root, text="button-1", width=8, height=2)
btn_open_folder.place(x=35, y=145)

# Entry for write path folder
ent_1_folder = Entry(root, width=25)
ent_1_folder.place(x=110, y=155)



# End programm
root.mainloop()

