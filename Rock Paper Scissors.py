from tkinter import *
import random


def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie, you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose, computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')


def reset():
    Result.set('')
    user_take.set('')


def exit():
    root.destroy()


root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title('Game - Rock, Paper, Scissors')
root.config(bg='mistyrose')

Label(root, text='Rock, Paper, Scissors', font='arial 22 bold', bg='hotpink').pack()

user_take = StringVar()
Label(root, text='Choose any one: Rock, Paper, Scissors', font='areal 15 bold', bg='pink2').place(x=10, y=70)
Entry(root, font='areal 18', textvariable=user_take, bg='azure').place(x=70, y=130)

comp_pick = random.randint(1, 3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
elif comp_pick == 3:
    comp_pick = 'scissors'

Result = StringVar()

Entry(root, font='arial 13 bold', textvariable=Result, bg='azure', width=40).place(x=15, y=250)
Button(root, font='arial 16 bold', text='PLAY', padx=5, bg='lavender', command=play).place(x=150, y=190)
Button(root, font='arial 14 bold', text='RESET', padx=5, bg='lemonchiffon', command=reset).place(x=70, y=310)
Button(root, font='arial 14 bold', text='EXIT', padx=5, bg='peachpuff', command=exit).place(x=230, y=310)

root.mainloop()














