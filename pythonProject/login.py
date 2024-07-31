import tkinter as tk
from tkinter import messagebox
from _datetime import datetime

def _timestamp():
    d = datetime.now()
    a = d.strftime("%d/%m/%y %H:%M:%S.%p ")
    return a
def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

    if userid == "admin" and password == "123":
        messagebox.showinfo("Login Successful", "Welcome, admin!")
        print("welcome! , ,,,,,one good book is equal to 100 frients ,,,,, " )
        print(        "Entry:   " ,_timestamp())
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def OnExit():
    print("Exit " , _timestamp())
    exit(1)


parent = tk.Tk()
parent.title("Login Form",)

username_label = tk.Label(parent, text="Userid:",font=("Arial Black", 11))
username_label.pack()

username_entry = tk.Entry(parent)
username_entry.pack()


password_label = tk.Label(parent, text="Password:",font=("Arial Black", 11))
password_label.pack()

password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
password_entry.pack()

login_button = tk.Button(parent, text="Login", command=validate_login,font=("Arial Black", 11))
login_button.pack()

Exit_button = tk.Button(parent, text="Exit",command=OnExit,font=("Arial Black", 11))
Exit_button.pack()

parent.mainloop()