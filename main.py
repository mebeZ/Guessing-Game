import random
import tkinter as tk
from tkinter import *

from PIL import Image, ImageTk

root = Tk()
root.title("Coin Flipping Game")
root.geometry('500x500')

l = Label(root, text="Coin Flipping Game")
l.config(font=("Courier", 14))

t = Text(root, width=52, height=5)
t.insert(INSERT, "Instructions: Flip the coin and observe the result.")

e = Button(root, text="Exit Game", bg='gray', fg='white', activebackground="lightgray", padx=40, pady=20, command=exit)
e.config(font=("Courier", 14))

#load heads
load = Image.open("heads.jpg")
load = load.resize((150, 150))
heads = ImageTk.PhotoImage(load)

#load tails
load = Image.open("tails.jpg")
load = load.resize((150, 150))
tails = ImageTk.PhotoImage(load)

i = Label(root, image=heads)

def flip():
    num = random.randint(0,1)
    if num == 0:
        i.config(image=heads)
    else:
        i.config(image=tails)

b = Button(root, text="Flip Coin", bg='lightblue', fg='white', activebackground="lightgray", padx=10, pady=10, command=flip)
b.config(font=("Courier", 8))

l.pack()
t.pack()
b.pack()
i.pack()
e.pack()

root.mainloop()


