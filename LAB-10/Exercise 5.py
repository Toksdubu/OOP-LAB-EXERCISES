# Module 6 - Tkinter GUI
# Exercise 5 - 5.3

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo, showerror, askyesnocancel

file_open = False
file_saved = True
file_path = ''


def openfile():
    global file_open, file_saved, file_path

    file_path = askopenfilename(title="Open File", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    print("Selected file:", file_path)

    if file_saved is True:
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                text_widget.delete('1.0', 'end')
                text_widget.insert('1.0', content)
                file_saved = False
                file_open = True
    else:
        result = askyesnocancel(
            title="Unsaved changes",
            message="Do you want to save before quitting?"
        )
        if result == YES:
            save_path = file_path
            with open(save_path, 'w') as file:
                content = text_widget.get('1.0', 'end-1c')
                file.write(content)
                file_saved = True
                file_open = False
        else:
            return


def savefile():
    global file_saved, file_open, file_path
    if file_open is True:
        if file_saved is False:
            showinfo(title="Unsaved Changes", message='There might be some changes need saving')

            save_path = asksaveasfilename(title="Save File", defaultextension=".txt",
                                          filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if save_path:
                with open(save_path, 'w') as file:
                    content = text_widget.get('1.0', 'end-1c')
                    file.write(content)
                    file_saved = True
                print("Selected save path:", save_path)

            else:
                file_saved = False
                print("The user chose no.")
        else:
            return

    else:
        showerror(title="No file", message="There is no file currently opened.")


def uppercase():
    global file_open
    if file_open is True:
        content = text_widget.get('1.0', 'end-1c')
        updated_content = content.upper()
        text_widget.delete('1.0', 'end')
        text_widget.insert('1.0', updated_content)
    else:
        showerror(title="No file", message="There is no file currently opened.")


def quit_file():
    global file_saved, file_path, file_open

    if file_saved is True:
        file_open = False
        quit()

    else:
        result1 = askyesnocancel(
            title="Unsaved changes",
            message="Do you want to save before quitting?"
        )
        if result1 == YES:
            with open(file_path, 'w') as file:
                content = text_widget.get('1.0', 'end-1c')
                file.write(content)
                file_saved = True
                file_open = False
                quit()
        else:
            return


def helpme():
    message = f'Menu Functions:\n\nFile:\nOpen - Open a new file\nSave - Save the existing file' \
              f'\nQuit - Quit the application\n\nEdit:\nConvert to upper - Convert the file contents to upper case' \
              f'\n\nAbout:\nHelp - Useful help\nAbout - Information about the application'
    showinfo(title='Help Instructions', message=message)


def about():
    message = f'Module 6 - Tkinter GUI\nLaboratory 10 - Exercise No.5\n\nSimple Text Editor' \
              f'\n\nCreated by: Aaron Paul E. Castillo' \
              f'\nBSCpE 1-6\n\nObject Oriented Programming'
    showinfo(title='About Information', message=message)


root = Tk()
root.title("Simple Text Editor")

text_widget = Text(root)
text_widget.pack()

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=False)
file_menu.add_command(label="Open", command=openfile)
file_menu.add_command(label="Save", command=savefile)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit_file)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=False)
edit_menu.add_command(label="Convert to Upper", command=uppercase)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

about_menu = Menu(menu_bar, tearoff=False)
about_menu.add_command(label="Help", command=helpme)
about_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="About", menu=about_menu)

root.mainloop()
