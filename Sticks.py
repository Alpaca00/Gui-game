from tkinter import *
from tkinter import messagebox
from tkinter import ttk as t
import random

root = Tk()
root.geometry('400x400+440+200')
root.title('TakeSticks')
#root.resizable(False, False)


pb = t.Progressbar(root, length=1000)
pb.pack()
pb.start(100)
pb.step(10)


l1 = Label(text="Welcome to our game ;)", bg="#1F252A", fg='white', height=3, font='cursive, 15')
l1.pack(fill=X)


e = Entry(root, bg='black', fg='Teal')
e.pack(fill=X)


rules = messagebox.showinfo('Rules', """The game is who takes the last stick is a loser.
\nAccording to the rules, the player must take 1 to 3 sticks.\n
A game starts with a random number.""")

num = [14, 15, 16, 18, 23, 24, 28]

text1=Text(root, font='cursive, 10', wrap=WORD, bg='black', fg='white')
text1.pack(fill=BOTH, expand=True)


scroll = Scrollbar(text1, command=text1.yview)
scroll.pack(fill=Y, side=RIGHT)
text1.config(yscrollcommand=scroll.set)


def showEnd(event):
    text1.see(END)
    text1.edit_modified(END)

text1.bind('<Motion>', showEnd)


def quit():
    answer = messagebox.askokcancel('Exit', 'Are you sure?')
    if answer == True:
        root.destroy()


amount = random.randint(13, 30)
if amount in num:
    amount += 1       

def get_num(number):
    global amount
    e.delete(0, END)
    e.insert(END, number)	
    amount -= number
    text1.insert(END, f'Taken:\t{number}\n')
    text1.insert(END, f'Remainder:\t{amount}\n')
    text1.insert(END, '-----------------------\n')
    taken_max = amount%4
    if taken_max > 3:
	    taken_max = 3
    if taken_max == 0:
        taken_max = 3
    else:
        taken_max -= 1
    if taken_max == 0:
        taken_max = 1
    amount -= taken_max     
    text1.insert(END, f'Artificial Intelligence:\t{taken_max}\n')
    text1.insert(END, f'Remainder after Artificial Intelligence:\t{amount}\n')
    if amount == 0 or amount < 0:
        text1.insert(END, 'Amigo wins;)')
        amount = random.randint(19,30)
    if amount == 1:
        text1.insert(END, 'Sorry Amigo, but remainder 1. You lose!\n\t\t\tRestart?')
        amount = random.randint(19,30)
 

def start():
    if btn_start['text'] == 'Start':
        text1.insert(END, f'\nHow many sticks do you want to take Amigo?\n\tRandom number to start: {amount}!\n')


pb.stop()


def restart():
    if btn_res['text'] == 'Restart':
        text1.delete('1.0', END)
        e.delete(0, END)
        text1.insert(END, f'\nHow many sticks do you want to take Amigo?\n\tRandom number to start: {amount}!\n')
    

frame2=Frame(root, bg='#1F252A')
frame2.pack(fill=X)


buttons = {'1': 1, '2': 2, '3': 3}

s = t.Style()
s.configure('Kim.TButton', foreground='maroon')

for k, v in buttons.items():
    t.Button(frame2, text=k, style='Kim.TButton', command=lambda number=v: get_num(number)).pack(fill=X, expand=1, side=LEFT)

frame1=Frame(root, bg='#1F252A')
frame1.pack(fill=X)

btn_start = t.Button(frame1, text='Start', style='Kim.TButton', command=start)
btn_start.pack(fill=X, expand=1, side=LEFT)

btn_res = t.Button(frame1, text='Restart', style='Kim.TButton', command=restart)
btn_res.pack(fill=X, expand=1, side=LEFT)

btn_exit = t.Button(frame1, text='Exit', style='Kim.TButton', command=quit)
btn_exit.pack(fill=X, expand=1, side=LEFT)


if __name__ == "__main__":
	root.mainloop()