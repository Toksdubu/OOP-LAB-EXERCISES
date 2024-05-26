# Module 6 = Tkinter
# Exercise 1
from tkinter import *


def clicked():
    print("Clicked")


app = Tk()
app.title("GUI Example 1")
app.geometry('200x200')

button1 = Button(app, text="Click Here", command=clicked)

button1.pack(side='bottom')


# Exercise 1.1
from tkinter import *


def clicked():
    print("-10 Ligtas Points")


app = Tk()
app.title("Clicker")
app.geometry('400x200')

button1 = Button(app, text="Do not click!", command=clicked)

button1.pack(side='top')

app.mainloop()
app.mainloop()
