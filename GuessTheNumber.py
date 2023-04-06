import random
import keyboard
from tkinter.ttk import *
from tkinter import *
window = Tk()
window.geometry("500x500")
window.configure(bg = "black")
triess = 0
tries = "Tries: "+str(triess)
dif = 0
randomN = ""

def rand():
    global randomN
    global dif
    if rb.get() == 1:
        dif = 50
    elif rb.get() == 2:
        dif = 100
    elif rb.get() == 3:
        dif = 200
    if dif != 0:
        randomN = random.randint(1, dif)
        rand.place_forget()
        triess = 0

def enter():
    global randomN
    global triess
    if randomN != "" and txt1.get() != "" and txt1.get().isnumeric() == True:
        triess = triess + 1
        tries = "Tries: " + str(triess)
        attempts = Label(window, text=tries, font=("arial", 16), bg="black", fg="green")
        attempts.place(x=220, y=340)
        txt = txt1.get()
        txt1.delete(0, END)
        if int(txt) == randomN and txt.isnumeric() == True:
            w = Label(window, image=scaled_corr, bg="black", height=100, width=100)
            w.place(x=50, y=280)
            rand.place(x=350, y=343)
            randomN = ""
        elif int(txt) < int(randomN) and txt.isnumeric() == True:
            h = Label(window, image=scaled_up, bg="black", height=80, width=62)
            h.place(x=70, y=280)
        elif int(txt) > int(randomN) and txt.isnumeric() == True:
            l = Label(window, image=scaled_down, bg="black", height=80, width=62)
            l.place(x=70, y=280)

rb = IntVar()
title = Label(window, text = "Guess The Number", fg = "lime", font = ("arial", 30), bg = "black")
title.place(x = 75, y = 5)
title = Label(window, text = "In this game you have to guess the random number\n Try to find it as fast as you can\n Good luck!", fg = "purple", font = ("pacifico  ", 15), bg = "black")
title.place(x = 25, y = 50)
txt1 = Entry(window)
txt1.place(x = 200, y = 300)
rand = Button(window, text = "Randomize", height = 2, width = 12, bg = "black", fg = "green", font = ("arial", 10), command = rand)
rand.place(x = 350, y = 343)
pick = Button(window, text = "Enter", height = 2, width = 12, bg = "black", fg = "green", font = ("arial", 10), command = enter)
pick.place(x = 350, y = 300)
attempts = Label(window, text = tries, font = ("arial", 16), bg = "black", fg = "green")
attempts.place(x = 220, y = 340)
d1 = Radiobutton(window, text = "Easy:(1-50)", bg = "purple", variable = rb, value = 1)
d1.place(x = 100, y = 400)
d2 = Radiobutton(window, text = "Medium:(1-100)", bg = "purple", variable = rb, value = 2)
d2.place(x = 200, y = 400)
d3 = Radiobutton(window, text = "Hard:(1-200)", bg = "purple", variable = rb, value = 3)
d3.place(x = 330, y = 400)
dice = PhotoImage(file ="../../GeneralExcercises/dice.png")
up = PhotoImage(file ="../../GeneralExcercises/up.png")
down = PhotoImage(file ="../../GeneralExcercises/down.png")
corr = PhotoImage(file ="../../GeneralExcercises/cor.png")
scaled_up = up.subsample(2)
scaled_down = down.subsample(2)
scaled_corr = corr.subsample(2)
sd = Label(window, image = dice, bg = "black", height = 150, width = 200)
sd.place(x = 170, y = 130)
keyboard.add_hotkey('Enter', enter)

window.mainloop()