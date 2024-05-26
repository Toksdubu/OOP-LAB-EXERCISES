# Module 6 - Tkinter
# Exercise 2

from tkinter import *

def clicked():
    global newText
    newText = e1.get()

    if len(newText) == 0:
        button1.config(bg="red", text="Clear")
    else:
        button1.config(bg="SystemButtonFace", text="Copy Text")
        e2.config(text=newText)
        e1.delete(0, END)

app = Tk()
app.title("Exercise 2")
app.geometry('200x100')

e2 = Label(text="Original Text")
e2.pack(side="bottom")
button1 = Button(app, text="Copy Text", command=clicked)
button1.pack(side='bottom')
e1 = Entry(app)
e1.pack(side='bottom')

app.mainloop()
