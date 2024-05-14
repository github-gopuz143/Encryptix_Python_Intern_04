import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Encryptix address book - Initialize window
root = Tk()
root.geometry('700x550')
root.config(bg='#d3f3f5')
root.title('Encryptix Contact Book')
root.resizable(0, 0)
contactlist = [
    ['Ammu', '369854712'],
    ['Priya Patil', '521155222'],
    ['Gauri', '521155222'],
    ['Abhi ', '78945614'],
    ['Gopu', '521155222'],
    ['Appu', '58745246'],
    ['lily', '521155345678'],
    ['Zoya', '23456898765'],
    ['riya', '2345000875'],
    ['Anju Paul', '5846975'],
    ['rose', '50843346'],
    ['Kiran Patel', '5647892'],
    ['Anjali Sharma', '89685320'],
    ['John', '98564785'],
    ['Monu', '85967412'],
    ['Julia', '85967412'],
    ['Arya', '850974452'],
    ['miwet', '85012347885'],
    ['tom', '81234567654'],
    ['Jim', '85967412'],
    ['xoxo', '85967136412'],
    ['yum', '146885967412'],

    ['Sreekuttan', '345678890']

]

Name = StringVar()
Number = StringVar()

# For creating frame
frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16), bg="#f0fffc", width=20, height=20,
                 borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


def Selected():
    print("hello", len(select.curselection()))
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])


# For add new contact
def AddContact():
    if Name.get() != "" and Number.get() != "":
        contactlist.append([Name.get(), Number.get()])
        print(contactlist)
        messagebox.showinfo("Confirmation", "Successfully Add New Contact")

    else:
        messagebox.showerror("Error", "Please fill the information")


def ViewContactList():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)

def UpdateDetail():
    if Name.get() and Number.get():
        contactlist[Selected()] = [Name.get(), Number.get()]

        messagebox.showinfo("Confirmation", "Successfully Update Contact")
        Select_set()

    elif not (Name.get()) and not (Number.get()) and not (len(select.curselection()) == 0):
        messagebox.showerror("Error", "Please fill the information")

    else:
        if len(select.curselection()) == 0:
            messagebox.showerror("Error", "Please Select the Name and \n press Load button")
        else:
            message1 = """To Load the all information of \n
                          selected row press Load button\n.
                          """
            messagebox.showerror("Error", message1)


def Delete_Entry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('Confirmation', 'You Want to Delete Contact\n Which you selected')
        if result == True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')


# exit game window
def EXIT():
    root.destroy()


def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)


Select_set()

# define buttons labels and entry widget
Label(root, text='Name', font=("Times new roman", 22, "bold"), bg='SlateGray3').place(x=30, y=20)
Entry(root, textvariable=Name, width=30).place(x=200, y=30)
Label(root, text='Contact No.', font=("Times new roman", 20, "bold"), bg='SlateGray3').place(x=30, y=70)
Entry(root, textvariable=Number, width=30).place(x=200, y=80)

Button(root, text=" ADD", font='Helvetica 18 bold', bg='#e8c1c7', command=AddContact, padx=20).place(x=50, y=140)
Button(root, text="EDIT", font='Helvetica 18 bold', bg='#e8c1c7', command=UpdateDetail, padx=20).place(x=50, y=200)
Button(root, text="DELETE", font='Helvetica 18 bold', bg='#e8c1c7', command=Delete_Entry, padx=20).place(x=50, y=260)
Button(root, text="VIEW", font='Helvetica 18 bold', bg='#e8c1c7', command=ViewContactList).place(x=50, y=325)
Button(root, text="EXIT", font='Helvetica 24 bold', bg='tomato', command=EXIT).place(x=250, y=470)

root.mainloop()
