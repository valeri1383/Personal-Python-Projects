from tkinter import *
import base64


def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)


def Mode():
    if (mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif (mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')


def exit():
    root.destroy()


def reset():
    Text.set('')
    private_key.set('')
    mode.set('')
    Result.set('')


root = Tk()
root.geometry('650x400')
root.resizable(0, 0)
root.title('Encode and Decode')
root.configure(bg='peach puff')

Label(root, text='ENCODE DECODE', font='arial 20 bold', bg='cyan').pack()
Label(root, text='Valery Project', font='arial 20 bold', bg='gold').pack(side=BOTTOM)

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

Label(root, font='arial 17 bold', text='Message', bg='peach puff').place(x=60, y=80)
Entry(root, font='aral 17', textvariable=Text, bg='light blue').place(x=320, y=80)

Label(root, font='arial 17 bold', bg='peach puff', text='KEY').place(x=60, y=110)
Entry(root, font='arial 17', textvariable=private_key, bg='light blue').place(x=320, y=110)

Label(root, font='arial 17 bold', bg='peach puff', text='MODE(e / d)').place(x=60, y=140)
Entry(root, font='arial 17', textvariable=mode, bg='light blue').place(x=320, y=140)

Entry(root, font='arial 17 bold', textvariable=Result, bg='light blue').place(x=320, y=170)

Button(root, font='arial 12 bold', text='RESULT', width=13, padx=2, bg='aquamarine', command=Mode).place(x=60, y=170)
Button(root, font='arial 15 bold', text='RESET', padx=2, width=6, command=reset, bg='lime green', ).place(x=150, y=250)
Button(root, font='arial 15 bold', text='EXIT', width=6, command=exit, bg='OrangeRed', padx=2, pady=2).place(x=350,
                                                                                                             y=250)

mainloop()
