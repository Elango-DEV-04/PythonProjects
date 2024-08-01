import csv
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def _timestamp():
    d = datetime.now()
    return d.strftime("%d/%m/%y %H:%M:%S.%p ")

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
    parent.title("Login Form")

    tk.Label(parent, text="Userid:", font=("Arial Black", 11)).grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(parent, font=("Arial Black", 11))
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(parent, text="Password:", font=("Arial Black", 11)).grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(parent, show="*", font=("Arial Black", 11))
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    login_button = tk.Button(parent, text="Login", font=("Arial Black", 11), command=validate_login)
    login_button.grid(row=2, columnspan=2, pady=10)

    parent.mainloop()

def main():
    def add_book():
        book_id = book_id_entry.get()
        book_title = book_title_entry.get().title()
        book_author = book_author_entry.get()

        if book_id == "" or book_title == "" or book_author == "":
            messagebox.showerror("Error", "Please fill all the fields!")
        else:
            with open("library.csv", "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([book_id, book_title, book_author, "Available"])
            messagebox.showinfo("Success", "Book added successfully!")
            book_id_entry.delete(0, tk.END)
            book_title_entry.delete(0, tk.END)
            book_author_entry.delete(0, tk.END)

    def search_book():
        search_value = search_entry.get().title()

        with open("library.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if search_value in row:
                    status = "Checked Out" if row[3] == "Checked Out" else "Available"
                    messagebox.showinfo("Book Details", f"Book ID: {row[0]}\nTitle: {row[1]}\nAuthor: {row[2]}\nStatus: {status}")
                    search_entry.delete(0, tk.END)
                    return

            messagebox.showerror("Error", "Book not found!")
            search_entry.delete(0, tk.END)

    def take_book():
        book_id = take_id_entry.get()
        updated = False

        with open("library.csv", "r") as file:
            rows = list(csv.reader(file))

        with open("library.csv", "w", newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row[0] == book_id:
                    if row[3] == "Available":
                        row[3] = "Checked Out"
                        updated = True
                    else:
                        messagebox.showinfo("Error", "Book is already checked out!")
                writer.writerow(row)

        if updated:
            messagebox.showinfo("Success", "Book checked out successfully!")
        take_id_entry.delete(0, tk.END)

    def return_book():
        book_id = return_id_entry.get()
        updated = False

        with open("library.csv", "r") as file:
            rows = list(csv.reader(file))

        with open("library.csv", "w", newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row[0] == book_id:
                    if row[3] == "Checked Out":
                        row[3] = "Available"
                        updated = True
                    else:
                        messagebox.showinfo("Error", "Book was not checked out!")
                writer.writerow(row)

        if updated:
            messagebox.showinfo("Success", "Book returned successfully!")
        return_id_entry.delete(0, tk.END)

    def on_exit():
        print("Exit:    ", _timestamp())
        root.destroy()

    root = tk.Tk()
    root.title("Library Management System")

    tk.Label(root, text="Book ID:", font=("Arial Black", 11), fg="gray").grid(row=0, column=0, padx=10, pady=10)
    book_id_entry = tk.Entry(root, borderwidth=2, width=25)
    book_id_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Title:", font=("Arial Black", 11), fg="gray").grid(row=1, column=0, padx=10, pady=10)
    book_title_entry = tk.Entry(root, borderwidth=2, width=25)
    book_title_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="Author:", font=("Arial Black", 11), fg="gray").grid(row=2, column=0, padx=10, pady=10)
    book_author_entry = tk.Entry(root, borderwidth=2, width=25)
    book_author_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(root, text="Search:", font=("Arial Black", 11), fg="gray").grid(row=3, column=0, padx=10, pady=10)
    search_entry = tk.Entry(root, borderwidth=2, width=25)
    search_entry.grid(row=3, column=1, padx=10, pady=10)

    tk.Label(root, text="Take Book ID:", font=("Arial Black", 11), fg="gray").grid(row=4, column=0, padx=10, pady=10)
    take_id_entry = tk.Entry(root, borderwidth=2, width=25)
    take_id_entry.grid(row=4, column=1, padx=10, pady=10)

    tk.Label(root, text="Return Book ID:", font=("Arial Black", 11), fg="gray").grid(row=5, column=0, padx=10, pady=10)
    return_id_entry = tk.Entry(root, borderwidth=2, width=25)
    return_id_entry.grid(row=5, column=1, padx=10, pady=10)

    add_button = tk.Button(root, text="Add Book", command=add_book, font=("Arial Black", 11))
    add_button.grid(row=6, column=0, pady=10)

    search_button = tk.Button(root, text="Search Book", command=search_book, font=("Arial Black", 11))
    search_button.grid(row=6, column=1, pady=10)

    take_button = tk.Button(root, text="Take Book", command=take_book, font=("Arial Black", 11))
    take_button.grid(row=7, column=0, pady=10)

    return_button = tk.Button(root, text="Return Book", command=return_book, font=("Arial Black", 11))
    return_button.grid(row=7, column=1, pady=10)

    exit_button = tk.Button(root, text="Exit", command=on_exit, font=("Arial Black", 11))
    exit_button.grid(row=8, column=0, columnspan=2, pady=10)

    root.mainloop()

login()
