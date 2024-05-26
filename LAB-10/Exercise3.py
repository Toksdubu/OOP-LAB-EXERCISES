# Module 6- Tkinter
# Exercise 3

from tkinter import *

app = Tk()
app.title("Exercise 3")
app.geometry('218x79')

frame1 = Frame(app)
frame1.pack(side="top", fill="x", expand=True)
label1 = Label(frame1, text="\t\t\t A \t\t\t", bg="red", borderwidth=5, relief='ridge')
label1.pack(side='top')


frame2 = Frame(app)
frame2.pack(side="top", fill="x", expand=False)
label3 = Label(frame2, text="\t B \t", bg="Yellow", borderwidth=5)
label3.pack(side='bottom')

label2 = Label(frame2, text="\t D \t", bg="White", borderwidth=5)
label2.pack(side='right', anchor="sw")

label4 = Label(frame2, text="\t C \t", bg="Blue", borderwidth=5)
label4.pack(side="bottom")



# Exercise 3.1 & 3.2

from tkinter import *

app = Tk()
app.title("Exercise 3.1 & 3.2")
app.geometry('200x100')

# Create frame
frame1 = Frame(app, bg="white", bd=10, relief='ridge')
frame1.pack(side="left", fill='both', expand=True)

# Create label A

frameA = Frame(frame1, bg='white', bd=10)
frameA.pack(side='top', fill="both", expand=True)
label1 = Label(frameA, text="A", fg="black", bg="white")
label1.pack(side="top", fill="both", expand=True)

# Create label B
frameB = Frame(frame1, bg='blue', bd=10)
frameB.pack(side='top', fill="both", expand=True)
label1 = Label(frameB, text="B", fg="black", background='blue')
label1.pack(side="top", fill="both", expand=True)

# Create frame2
frame2 = Frame(app, bg="white", bd=10, relief='ridge')
frame2.pack(side="left", fill='both', expand=True)

# Create label B

frameC = Frame(frame2, bg='blue', bd=10)
frameC.pack(side='top', fill="both", expand=True)
label1 = Label(frameC, text="C", fg="black", bg="blue")
label1.pack(side="top", fill="both", expand=True)

# Create label C
frameD = Frame(frame2, bg='white', bd=10)
frameD.pack(side='top', fill="both", expand=True)
label1 = Label(frameD, text="D", fg="black", background='white')
label1.pack(side="top", fill="both", expand=True)

app.mainloop()
app.mainloop()
