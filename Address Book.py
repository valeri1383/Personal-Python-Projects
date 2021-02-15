from tkinter import *

root = Tk()
root.geometry('400x400')
root.configure(bg='cyan')
root.resizable(1, 1)
root.title('Address Book')

contact_list = [
    ['John Smith', '07567374343'],
    ['Terry Adams', '07569984343'],
    ['Allen Gibson', '07564474743'],
    ['Grant Foster', '07567396843'],
    ['Hall Grey', '07567746343']
]

Name = StringVar()
Number = StringVar()
frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame,bg='light goldenrod', yscrollcommand=scroll.set, width=30, height=33)
scroll.configure(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


def Selected():
    return int(select.curselection()[0])


def AddContact():
    contact_list.append([Name.get(), Number.get()])
    Select_set()


def EDIT():
    contact_list[Selected()] = [Name.get(), Number.get()]
    Select_set()


def DELETE():
    del contact_list[Selected()]
    Select_set()


def VIEW():
    NAME, PHONE = contact_list[Selected()]
    Name.set(NAME)
    Number.set(PHONE)


def EXIT():
    root.destroy()


def RESET():
    Name.set('')
    Number.set('')


def Select_set():
    contact_list.sort()
    select.delete(0, END)
    for name, phone in contact_list:
        select.insert(END, name)


Select_set()

Label(root, text='NAME', font='arial 15 bold', bg='cyan').pack()
Entry(root, font=20, bg='light yellow', textvariable=Name).pack()

Label(root, text='PHONE NO.', font='arial 15 bold', bg='cyan').pack()
Entry(root, font=20,bg='light yellow', textvariable=Number).pack()

Button(root, text='ADD', width=7, font='arial 15 bold', bg='SlateGray4', command=AddContact).pack()
Button(root, text='EDIT', width=7, font='arial 15 bold', bg='SlateGray4', command=EDIT).pack()
Button(root, text="DELETE", width=7, font='arial 15 bold', bg='SlateGray4', command=DELETE).pack()
Button(root, text="VIEW", width=7, font='arial 15 bold', bg='SlateGray4', command=VIEW).pack()
Button(root, text="EXIT", width=7, font='arial 15 bold', bg='tomato', command=EXIT).pack()
Button(root, text="RESET", width=7, font='arial 15 bold', bg='SlateGray4', command=RESET).pack()

mainloop()
