from tkinter import *
from tkinter import messagebox
from random import *
from turtle import xcor
from pygame import *
from tkinter import PhotoImage
from getpass import *
import getpass


tk = Tk() 

# Stingvar the login
username = StringVar()
password = StringVar()
again_passw = StringVar()
gmail = StringVar()

def message_succefulLOGIN():
    messagebox.showinfo("Registrired succeful!", "Username"  f'{username}'  "has been registrired succefful!")

# Auto for registration
def strs_registr():
    username_info = username.get()
    password_info = password.get()
    again_passwd_info = again_passw.get()
    gmail_info = gmail.get()
    print(username_info, password_info, again_passwd_info, gmail_info)
    
    file = open("login.txt", "w")
    file.write(" Username: " + username_info)
    file.write(" Password: " + password_info)
    file.close()

    file1 = open("gmail.txt", "w") 
    file1.write( "Gmail: " + gmail_info)
    file1.close()

# Text ifo the entry
def click_ent1(event):
    ent1.config(state=NORMAL)
    ent1.delete(0, END)

def click_ent2(event):
    ent2.config(state=NORMAL)
    ent2.delete(0, END)

def click_ent3(event):
    ent3.config(state=NORMAL)
    ent3.delete(0, END)

def click_ent4(event):
    ent4.config(state=NORMAL)
    ent4.delete(0, END)


    # Entry for entered password, name and gmail
ent1 = Entry(tk, width=20, bg="light gray", font=("Comic", 20), textvariable=again_passw)
ent1.place(x=55, y=270)
ent1.insert(2, "Enter again password")
ent1.config(state=DISABLED)
ent1.bind("<Button-1>", click_ent1)

ent2 = Entry(tk, width=20, bg="light gray", font=("Arial", 20), textvariable=password)
ent2.place(x=55, y=230)
ent2.insert(2, "Enter password")
ent2.config(state=DISABLED)
ent2.bind("<Button-1>", click_ent2)

ent3 = Entry(tk, width=20, bg="light gray", font=("Arial", 20), textvariable=username)
ent3.place(x=55, y=190)
ent3.insert(2, "Enter username")
ent3.config(state=DISABLED)
ent3.bind("<Button-1>", click_ent3)

ent4 = Entry(tk, width=20, bg="light gray", font=("Arial", 20), textvariable=gmail)
ent4.place(x=55, y=150)
ent4.insert(2, "Enter gmail")
ent4.config(state=DISABLED)
ent4.bind("<Button-1>", click_ent4)

    # message for meesagers on the open in account (This is inccorent or succefful)
def message_succeffulOpenAccount():
    messagebox.showinfo("Succefful!", "Your succefful open on the account!")

def message_failedOpenAccount():
    messagebox.showerror('Error!', 'Your inccorent or no enter password or username!')
    messagebox.showinfo('Error!', 'Your again enter password and username.')

# Start work on account Penstagram
def Windows_links():
    tk3 = Tk()

    tk3.title("Penstagram")
    tk3.geometry("410x500")
    tk3.resizable(True, True)
    tk3.configure(bg="white")

    # One buttons for message , open yours account , message , ribbon and search
    photo1 = PhotoImage(file="")

    # Button for photo one message
    btn_photo1 = Button(tk3, text="Search", image=photo1)
    btn_photo1.place()

    # Two buttons for message , open yours account , message , ribbon and search
    photo2 = PhotoImage(file="")

    # Button for photo two message
    btn_photo2 = Button(tk3, text="Account", image=photo2)
    btn_photo2.place(x=10, y=10)

    # Three buttons for message , open yours account , message , ribbon and search
    photo3 = PhotoImage(file="")

    # Button for photo three message
    btn_photo3 = Button(tk3, text="Message", image=photo3)
    btn_photo3.place()


    username_lbl_consulision = Label(tk3, text=getpass.getuser(ent3 + click_ent3))
    username_lbl_consulision.place()

    lbl_penstagram1 = Label(tk3, text="PENSTAGRAM")
    lbl_penstagram1.place(x=10, y=10)

    lbl_versionPENSTA = Label(tk3, text="2.0")
    lbl_versionPENSTA.place(x=10, y=50)

    tk3.mainloop()

# Open your on the account Penstagram
def New_Window():
    # Close two windows(tk2)
    def close_tk2():
        tk2.destroy()

    # Open one widows(tk)
    def open_tk():
        print(tk)
        
    def ent1_username_click(event):
        ent1_username.config(state=NORMAL)
        ent1_username.delete(0, END)

    def ent2_password_click(event):
        ent2_password.config(state=NORMAL)
        ent2_password.delete(0, END)

    tk2 = Tk()
    tk2.title("Penstagram")
    tk2.geometry("410x500")
    tk2.resizable(False, False)
    tk2.configure(bg="white")

    # Enter your password and login for open links
    def OpenLogin():
        password2_info = password2.get()
        username2_info = username2.get()
        print(username2_info, password2_info)

        file2 = open('login.txt', 'r')
        file2.read(1)
        file2.close()
        print(password2_info , username2_info)


    username2 = StringVar()
    password2 = StringVar()
    
    ent1_username = Entry(tk2, width=20, bg="light gray", font=("Comic", 20), textvariable=username2)
    ent1_username.place(x=60, y=120)
    ent1_username.insert(2, "Enter username")
    ent1_username.config(state=DISABLED)
    ent1_username.bind("<Button-1>", ent1_username_click)

    ent2_password = Entry(tk2, width=20, bg="light gray", font=("Comic", 20), textvariable=password2)
    ent2_password.place(x=60, y=170)
    ent2_password.insert(2, "Enter password") 
    ent2_password.config(state=DISABLED)
    ent2_password.bind("<Button-1>", ent2_password_click)

    # For succefful or failed open on the account
    def authorized_account():
        if ent1_username and ent2_password:
            message_succeffulOpenAccount()
            OpenLogin()
        else:
            message_failedOpenAccount()

    lbl1_tk2 = Label(tk2, text="PENSTAGRAM", font="Comic", bg="white", fg="light gray")
    lbl1_tk2.place(x=145, y=80)

    lbl2_tk2 = Label(tk2, text="2.0", font="Arial, 13", bg="white", fg="light gray")
    lbl2_tk2.place(x=265, y=70)

    btn_login = Button(tk2, text="Open Account", bg="purple", fg="white", width=15, height=1, font="Comic", command=lambda:[OpenLogin(), authorized_account(),Windows_links()])
    btn_login.place(x=120, y=240)

    btn_cancel = Button(tk2, text="Cancel", bg="purple", fg="white", width=7, height=1, font="Comic, 10", command=lambda:[open_tk(), close_tk2()])
    btn_cancel.place(x=180, y=290)

    tk2.mainloop()

tk.geometry("410x500")
tk.title("Penstagram")
tk.resizable(False, False)

# Close registration on window(tk)
def close_programms():
    tk.destroy()

# Text for windows
lbl1 = Label(tk, text="Sign up for", fg="black", font="Comic, 17", bg="white")
lbl1.place(x=157, y=50)

lbl2 = Label(tk, text="PENSTAGRAM", font="Comic", bg="white", fg="light gray") 
lbl2.place(x=145, y=90)

lbl3 = Label(tk, text="2.0", font="Arial, 13", bg="white", fg="light gray")
lbl3.place(x=265, y=80)
    
# Button for registred
btn_reg1 = Button(tk, text="Sign Up", bg="purple", fg="white", width=15, height=2, font="Comic", command=lambda:[strs_registr(), message_succefulLOGIN(), Windows_links()])
btn_reg1.place(x=116, y=320)

btn_reg2 = Button(tk, text="Log In", width=19, height=1, bg="purple", fg="white", font="Comic", command=lambda:[close_programms(), New_Window()])
btn_reg2.place(x=95, y=420)

# Color for window
tk.minsize(10, 10)
tk.configure(bg="white")

# End the progamms
tk.mainloop()

