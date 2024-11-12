from tkinter import *
from tkinter import Tk
from tkinter import Button
from tkinter import Label

root = Tk()

root.title("Glasses")
root.geometry("450x450")
root.resizable(True, True)

btn_open_folder = Button(root, text="button-1", width=8, height=2)
btn_open_folder.place(x=35, y=145)



root.mainloop()

