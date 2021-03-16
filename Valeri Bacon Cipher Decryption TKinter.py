from tkinter import *

lookup = {'a': 'aaaaa', 'b': 'aaaab', 'c': 'aaaba', 'd': 'aaabb', 'e': 'aabaa',
          'f': 'aabab', 'g': 'aabba', 'h': 'aabbb', 'i': 'abaaa', 'j': 'abaab',
          'k': 'ababa', 'l': 'ababb', 'm': 'abbaa', 'n': 'abbab', 'o': 'abbba',
          'p': 'abbbb', 'q': 'baaaa', 'r': 'baaab', 's': 'baaba', 't': 'baabb',
          'u': 'babaa', 'v': 'babab', 'w': 'babba', 'x': 'babbb', 'y': 'bbaaa',
          'z': 'bbaab'}


''' Bacon encrypting function '''
def encrypt_with_bacon(text):
    cipher = ''
    for letter in text:
        if letter != ' ':
            cipher += lookup[letter]
        else:
            cipher += ' '
    return cipher


''' Bacon decrypting function '''
def decrypt_with_bacon(text):
    decipher = ''
    i = 0

    while True:
        if i < len(text) - 4:
            substr = text[i:i + 5]
            if substr[0] != ' ':
                decipher += list(lookup.keys())[list(lookup.values()).index(substr)]
                i += 5
            else:
                decipher += ' '
                i += 1
        else:
            break
    return decipher



def Mode():
    if (mode.get() == 'e'):
        Result.set(encrypt_with_bacon(Text.get()))
    elif (mode.get() == 'd'):
        Result.set(decrypt_with_bacon(Text.get()))
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
root.title('Encode and Decode with Bacon cipher')
root.configure(bg='peach puff')

Label(root, text='ENCODE and DECODE', font='arial 20 bold', bg='cyan').pack()
Label(root, text='Valeri Bacon Cipher Project', font='arial 20 bold', bg='gold').pack(side=BOTTOM)

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

Label(root, font='arial 17 bold', text='Message', bg='peach puff').place(x=60, y=110)
Entry(root, font='aral 17', textvariable=Text, bg='light blue').place(x=320, y=110)


Label(root, font='arial 17 bold', bg='peach puff', text='MODE(e / d)').place(x=60, y=140)
Entry(root, font='arial 17', textvariable=mode, bg='light blue').place(x=320, y=140)

Entry(root, font='arial 17 bold', textvariable=Result, bg='light blue').place(x=320, y=170)

Button(root, font='arial 12 bold', text='RESULT', width=13, padx=2, bg='aquamarine', command=Mode).place(x=60, y=170)
Button(root, font='arial 15 bold', text='RESET', padx=2, width=6, command=reset, bg='lime green', ).place(x=150, y=250)
Button(root, font='arial 15 bold', text='EXIT', width=6, command=exit, bg='OrangeRed', padx=2, pady=2).place(x=350,
                                                                                                             y=250)

mainloop()