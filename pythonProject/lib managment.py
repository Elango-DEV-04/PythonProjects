import csv
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from _datetime import datetime

def _timestamp():
    d = datetime.now()
    a = d.strftime("%d/%m/%y %H:%M:%S.%p ")
    return a

def login():
    def validate_login():
        userid = username_entry.get()
        password = password_entry.get()
        if userid == "admin" and password == "123":
            messagebox.showinfo("Login Successful", "Welcome, admin!")
            print("welcome! , ,,,,,one good book is equal to 100 friends ,,,,, ")
            print("Entry:   ", _timestamp())
            parent.destroy()
            main()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    parent = tk.Tk()
    parent.title("Login Form", )

    username_label = tk.Label(parent, text="Userid:",font=("Arial Black", 11))
    username_label.grid(row=0,column=)
    un = ""
    username_entry = tk.Entry(parent,textvariable=un,takefocus=True)
    un = username_entry.get()
    username_entry.pack()

    password_label = tk.Label(parent, text="Password:", font=("Arial Black", 11))
    password_label.pack()
    ps = ""
    password_entry = tk.Entry(parent, show="*",textvariable=ps,takefocus=True)  # Show asterisks for password
    ps = password_entry.get()
    password_entry.pack()


    login_button = tk.Button(parent, text="Login",font=("Arial Black", 11),command=validate_login)
    login_button.pack()
    parent.mainloop()


def main():
    def add_book():

        book_id = book_id_entry.get()
        book_title = book_title_entry.get().title()
        book_author = book_author_entry.get()

        if book_id == "" or book_title == "" or book_author == "":
            messagebox.showerror("Error", "Please fill all the fields!")
        else:

            with open("library.csv", "a") as file:
                writer = csv.writer(file)

                writer.writerow([book_id, book_title, book_author])

            messagebox.showinfo("Success", "Book added successfully!")

            book_id_entry.delete(0, END)
            book_title_entry.delete(0, END)
            book_author_entry.delete(0, END)

    def search_book():

        search_value = search_entry.get().title()

        with open("library.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:

                if search_value in row:
                    messagebox.showinfo("Book Details", f"Book ID: {row[0]}\nTitle: {row[1]}\nAuthor: {row[2]}")

                    search_entry.delete(0, END)
                    return

            messagebox.showerror("Error", "Book not found!")

            search_entry.delete(0, END)

    def OnExit():
        print("Exit:    ", _timestamp())
        exit(1)

    root = Tk()
    root.title("Library Management System")
   

    Label(root, text="Book ID:", font=("Arial Black", 11), fg="gray").grid(row=0, column=0)
    book_id_entry = Entry(root, borderwidth=2, width=19)
    book_id_entry.grid(row=0, column=1)

    Label(root, text="Title:", font=("Arial Black", 11), fg="gray").grid(row=1, column=0)
    book_title_entry = Entry(root, borderwidth=2, width=19)
    book_title_entry.grid(row=1, column=1)

    Label(root, text="Author:", font=("Arial Black", 11), fg="gray").grid(row=2, column=0)
    book_author_entry = Entry(root, borderwidth=2, width=19)
    book_author_entry.grid(row=2, column=1)

    Label(root, text="Search:", font=("Arial Black", 11), fg="gray").grid(row=3, column=0)
    search_entry = Entry(root, borderwidth=2, width=19)
    search_entry.grid(row=3, column=1)

    add_button = Button(root, text="Add Book", command=add_book, font=("Arial Black", 11))
    add_button.grid(row=4, column=0)

    search_button = Button(root, text="Search Book", command=search_book, font=("Arial Black", 11))
    search_button.grid(row=4, column=1)

    Exit_button = Button(root, text="Exit", command=OnExit, font=("Arial Black", 11))
    Exit_button.grid(row=4, column=3)

    root.mainloop()
login()