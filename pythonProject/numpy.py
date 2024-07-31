from tkinter import *
import random
import os
import sys
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#5B2C6F")
        self.root.title("Billing Software")
        title = Label(self.root, text="Billing System", bd=12, relief=RIDGE, font=("Arial Black", 20), bg="#A569BD",
                      fg="white").pack(fill=X)
        self.mango = IntVar()
        self.apple = IntVar()
        self.banana = IntVar()
        self.cherry = IntVar()
        self.orange = IntVar()
        self.papaya = IntVar()
        self.pear = IntVar()
        self.tomato = IntVar()
        self.potato = IntVar()
        self.carrot = IntVar()
        self.pumpkin = IntVar()
        self.onion = IntVar()
        self.total_sna = StringVar()
        self.total_gro = StringVar()
        self.total_hyg = StringVar()
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.c_name = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.phone = StringVar()

        details = LabelFrame(self.root, text="Customer Details", font=("Arial Black", 12), bg="#A569BD", fg="white",
                             relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)
        cust_name = Label(details, text="Customer Name", font=("Arial Black", 14), bg="#A569BD", fg="white").grid(row=0,
                                                                                                                  column=0,
                                                                                                                  padx=15)

        cust_entry = Entry(details, borderwidth=4, width=30, textvariable=self.c_name).grid(row=0, column=1, padx=8)

        contact_name = Label(details, text="Contact No.", font=("Arial Black", 14), bg="#A569BD", fg="white").grid(
            row=0, column=2, padx=10)

        contact_entry = Entry(details, borderwidth=4, width=30, textvariable=self.phone).grid(row=0, column=3, padx=8)

        bill_name = Label(details, text="Bill.No.", font=("Arial Black", 14), bg="#A569BD", fg="white").grid(row=0,
                                                                                                             column=4,
                                                                                                             padx=10)

        bill_entry = Entry(details, borderwidth=4, width=30, textvariable=self.bill_no).grid(row=0, column=5, padx=8)

        Fruits = LabelFrame(self.root, text="Friuts", font=("Arial Black", 12), bg="#E5B4F3", fg="#6C3483",
                            relief=GROOVE, bd=10)
        Fruits.place(x=5, y=180, height=380, width=325)

        item1 = Label(Fruits, text="apple", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=0, column=0,
                                                                                                       pady=11)
        item1_entry = Entry(Fruits, borderwidth=2, width=15, textvariable=self.apple).grid(row=0, column=1, padx=10)

        item2 = Label(Fruits, text="orange(1 Pack)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=1,
                                                                                                                column=0,
                                                                                                                pady=11)
        item2_entry = Entry(Fruits, borderwidth=2, width=15, textvariable=self.orange).grid(row=1, column=1, padx=10)

        item3 = Label(Fruits, text="mango(10Rs)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=2,
                                                                                                             column=0,
                                                                                                             pady=11)
        item3_entry = Entry(Fruits, borderwidth=2, width=15, textvariable=self.mango).grid(row=2, column=1, padx=10)

        item4 = Label(Fruits, text="papaya(20Rs)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=3,
                                                                                                              column=0,
                                                                                                              pady=11)
        item4_entry = Entry(Fruits, borderwidth=2, width=15, textvariable=self.papaya).grid(row=3, column=1, padx=10)

        item5 = Label(Fruits, text="pear", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=4, column=0,
                                                                                                      pady=11)
        item5_entry = Entry(Fruits, borderwidth=2, width=15, textvariable=self.pear).grid(row=4, column=1, padx=10)

        vegetable = LabelFrame(self.root, text="vegetable", font=("Arial Black", 12), relief=GROOVE, bd=10,
                               bg="#E5B4F3", fg="#6C3483")
        vegetable.place(x=340, y=180, height=380, width=325)

        item8 = Label(vegetable, text="tomato(1kg)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=0,
                                                                                                                column=0,
                                                                                                                pady=11)
        item8_entry = Entry(vegetable, borderwidth=2, width=15, textvariable=self.tomato).grid(row=0, column=1, padx=10)

        item9 = Label(vegetable, text="potato(1kg)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=1,
                                                                                                                column=0,
                                                                                                                pady=11)
        item9_entry = Entry(vegetable, borderwidth=2, width=15, textvariable=self.potato).grid(row=1, column=1, padx=10)

        item10 = Label(vegetable, text="carrot(1kg)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=2,
                                                                                                                 column=0,
                                                                                                                 pady=11)
        item10_entry = Entry(vegetable, borderwidth=2, width=15, textvariable=self.carrot).grid(row=2, column=1,
                                                                                                padx=10)

        item11 = Label(vegetable, text="pumpkin", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=3,
                                                                                                             column=0,
                                                                                                             pady=11)
        item11_entry = Entry(vegetable, borderwidth=2, width=15, textvariable=self.pumpkin).grid(row=3, column=1,
                                                                                                 padx=10)

        item12 = Label(vegetable, text="onion", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=4,
                                                                                                           column=0,
                                                                                                           pady=11)
        item12_entry = Entry(vegetable, borderwidth=2, width=15, textvariable=self.onion).grid(row=4, column=1, padx=10)

        billarea = Frame(self.root, bd=10, relief=GROOVE, bg="#E5B4F3")
        billarea.place(x=1010, y=188, width=330, height=372)

        bill_title = Label(billarea, text="Bill Area", font=("Arial Black", 17), bd=7, relief=GROOVE, bg="#E5B4F3",
                           fg="#6C3483").pack(fill=X)

        scrol_y = Scrollbar(billarea, orient=VERTICAL)
        self.txtarea = Text(billarea, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        billing_menu = LabelFrame(self.root, text="Billing Summery", font=("Arial Black", 12), relief=GROOVE, bd=10,
                                  bg="#A569BD", fg="white")
        billing_menu.place(x=0, y=560, relwidth=1, height=137)

        self.total_Fruits = Label(billing_menu, text="Total Fruits Price", font=("Arial Black", 11), bg="#A569BD",
                                  fg="white").grid(row=0, column=0)
        self.total_Fruits_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_sna).grid(row=0,
                                                                                                                 column=1,
                                                                                                                 padx=10,
                                                                                                                 pady=7)

        self.total_vegetable = Label(billing_menu, text="Total vegetable Price", font=("Arial Black", 11), bg="#A569BD",
                                     fg="white").grid(row=1, column=0)
        self.total_vegetable_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_gro).grid(
            row=1, column=1, padx=10, pady=7)

        self.tax_Fruits = Label(billing_menu, text="Fruits Tax", font=("Arial Black", 11), bg="#A569BD",
                                fg="white").grid(row=0, column=2)
        self.tax_Fruits_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.a).grid(row=0, column=3,
                                                                                                       padx=10, pady=7)

        self.tax_vegetable = Label(billing_menu, text="vegetable Tax", font=("Arial Black", 11), bg="#A569BD",
                                   fg="white").grid(row=1, column=2)
        self.tax_vegetable_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.b).grid(row=1,
                                                                                                          column=3,
                                                                                                          padx=10,
                                                                                                          pady=7)

        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#6C3483")
        button_frame.place(x=830, width=500, height=95)

        self.button_total = Button(button_frame, text="Total Bill", font=("Arial Black", 15), pady=10, bg="#E5B4F3",
                                   fg="#6C3483", command=lambda: total(self)).grid(row=0, column=0, padx=12)
        self.button_clear = Button(button_frame, text="Clear Field", font=("Arial Black", 15), pady=10, bg="#E5B4F3",
                                   fg="#6C3483", command=lambda: clear(self)).grid(row=0, column=1, padx=10, pady=6)
        self.button_exit = Button(button_frame, text="Exit", font=("Arial Black", 15), pady=10, bg="#E5B4F3",
                                  fg="#6C3483", width=8, command=lambda: exit1(self)).grid(row=0, column=2, padx=10,
                                                                                           pady=6)
        intro(self)


def total(self):
    if (self.c_name.get == "" or self.phone.get() == ""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.ma = self.mango.get() * 120
    self.ap = self.apple.get() * 40
    self.ba = self.banana.get() * 10
    self.ch = self.cherry.get() * 20
    self.ra = self.orange.get() * 10
    self.pa = self.papaya.get() * 30
    self.pe = self.pear.get() * 60
    total_Fruits_price = (self.ma + self.ap + self.ba + self.ch + self.ra + self.pa + self.pe)
    self.total_sna = str(total_Fruits_price) + " Rs"
    self.a.set(str(round(self.total_Fruits_price * 0.05, 3)) + " Rs")

    self.to = self.tomato.get() * 42
    self.po = self.potato.get() * 120
    self.co = self.corrat.get() * 113
    self.pu = self.pumpkin.get() * 160
    self.on = self.onion.get() * 55
    total_vegetables_price = (self.to + self.po + self.co + self.pu + self.on)
    self.total_Vege.set(str(total_vegetables_price) + " Rs")
    self.b.set(str(round(total_vegetables_price * 0.01, 3)) + " Rs")

    self.total_all_bill = (total_Fruits_price + total_vegetables_price + (round(total_Fruits_price * 0.01, 3)) + (
        round(total_vegetables_price * 0.10, 3)))

    self.total_all_bil = str(self.total_all_bill) + " Rs"
    billarea(self)


def intro(self):
    self.txtarea.delete(1.0, END)
    self.txtarea.insert(END, "\tWELCOME TO SUPER MARKET\n\tPhone-No.739275410")
    self.txtarea.insert(END, f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END, f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END, "\n====================================\n")
    self.txtarea.insert(END, "\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END, "\n====================================\n")


def billarea(self):
    intro(self)
    if self.mango.get() != 0:
        self.txtarea.insert(END, f"Mango\t\t {self.mango.get()}\t{self.ma}\n")
    if self.apple.get() != 0:
        self.txtarea.insert(END, f"Apple\t\t {self.apple.get()}\t{self.ap}\n")
    if self.banana.get() != 0:
        self.txtarea.insert(END, f"Banana\t\t {self.banana.get()}\t{self.ba}\n")
    if self.cherry.get() != 0:
        self.txtarea.insert(END, f"Cherry\t\t {self.cherry.get()}\t{self.ch}\n")
    if self.orange.get() != 0:
        self.txtarea.insert(END, f"Orange\t\t {self.orange.get()}\t{self.ra}\n")
    if self.papaya.get() != 0:
        self.txtarea.insert(END, f"Papaya\t\t {self.papaya.get()}\t{self.pa}\n")
    if self.pear.get() != 0:
        self.txtarea.insert(END, f"Pear\t\t {self.pear.get()}\t{self.pe}\n")
    if self.tomato.get() != 0:
        self.txtarea.insert(END, f"Tomato\t\t {self.tomato.get()}\t{self.to}\n")
    if self.potato.get() != 0:
        self.txtarea.insert(END, f"potato\t\t {self.potato.get()}\t{self.po}\n")
    if self.carrot.get() != 0:
        self.txtarea.insert(END, f"carrot\t\t {self.carrot.get()}\t{self.ca}\n")
    if self.pumpkin.get() != 0:
        self.txtarea.insert(END, f"pumpkin\t\t {self.pumpkin.get()}\t{self.pu}\n")
    if self.onion.get() != 0:
        self.txtarea.insert(END, f"onion\t\t {self.onion.get()}\t{self.on}\n")

    self.txtarea.insert(END, f"------------------------------------\n")
    if self.a.get() != "0.0 Rs":
        self.txtarea.insert(END, f"Total Fruits Tax : {self.a.get()}\n")
    if self.b.get() != "0.0 Rs":
        self.txtarea.insert(END, f"Total Vegetable Tax : {self.b.get()}\n")

    self.txtarea.insert(END, f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END, f"------------------------------------\n")


def clear(self):
    self.txtarea.delete(1.0, END)
    self.mango.set(0)
    self.banana.set(0)
    self.apple.set(0)
    self.cherry.set(0)
    self.orange.set(0)
    self.papaya.set(0)
    self.pear.set(0)
    self.tomato.set(0)
    self.potato.set(0)
    self.corrat.set(0)
    self.pumpkin.set(0)
    self.onion.set(0)
    self.total_sna.set(0)
    self.total_gro.set(0)
    self.total_hyg.set(0)
    self.a.set(0)
    self.b.set(0)
    self.c.set(0)
    self.c_name.set(0)
    self.bill_no.set(0)
    self.bill_no.set(0)
    self.phone.set(0)


def exit1(self):
    self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()
