# Module 6 - Tkinter
# Exercise 4

from tkinter import *


def draw_shape(event):
    x = event.x
    y = event.y

    # Check if the pressed key is 's' for square or 'c' for circle
    if current_shape == 's':
        shape = canvas.create_rectangle(x, y, x + 50, y + 50, outline=current_color, fill=current_fill)
    elif current_shape == 'c':
        shape = canvas.create_oval(x, y, x + 50, y + 50, outline=current_color, fill=current_fill)


def handle_keypress(event):
    global current_shape, current_fill, current_color

    # Shape key mappings: 's' for square, 'c' for circle
    if event.char in ['s', 'c']:
        current_shape = event.char

    # Color key mappings: 'y' for yellow, 'r' for red
    # Filling key mappings: 'F' for filled, 'f' for unfilled
    elif event.char in ['F', 'f']:
        current_fill = current_color if event.char == 'F' else ''

    elif event.char in ['y', 'r']:
        current_fill = '' if event.char == ['y', 'r'] else None
        current_color = 'yellow' if event.char == 'y' else 'red'


def red():
    global current_color, current_fill
    current_fill = ''
    current_color = "red"


def yellow():
    global current_color, current_fill
    current_fill = ''
    current_color = "yellow"


def fill():
    global current_color, current_fill
    current_fill = current_color


def unfill():
    global current_fill
    current_fill = ''


def square():
    global current_shape, current_fill, current_color
    current_shape = "s"


def circle():
    global current_shape, current_fill, current_color
    current_shape = 'c'


app = Tk()
app.title("Shape Drawing")
app.geometry('400x300')

menu1 = Menu(app)
app.config(menu=menu1)

Menu_bar = Menu(menu1, tearoff=False)
Menu_bar.add_command(label="Square", command=square)
Menu_bar.add_command(label="Circle", command=circle)
menu1.add_cascade(label='Shapes', menu=Menu_bar)

colorMenu = Menu(menu1, tearoff=False)
colorMenu.add_command(label="Red", command=red)
colorMenu.add_command(label="Yellow", command=yellow)
menu1.add_cascade(label='Colors', menu=colorMenu)

fillMenu = Menu(menu1, tearoff=False)
fillMenu.add_command(label="Filled", command=fill)
fillMenu.add_command(label="Unfilled", command=unfill)
menu1.add_cascade(label='Fill', menu=fillMenu)


canvas = Canvas(app, width=400, height=300, bg="blue")
canvas.pack()

current_shape = 's'  # Default shape is square
current_fill = ''    # Default filling is unfilled
current_color = 'yellow'  # Default color is yellow

canvas.bind("<Button-3>", circle)
canvas.bind("<Button-2>", square)
canvas.bind("<Button-1>", draw_shape)
app.bind("<Key>", handle_keypress)


app.mainloop()
