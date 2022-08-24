from tkinter.filedialog import *
import tkinter as tk

def saveFile():
    new_file = asksaveasfile(mode = 'w', filetype = [('text files', '.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode = 'r', filetype = [('text files', '*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)

def clearFile():
    entry.delete(1.0, END)

newWindow = tk.Tk()
newWindow.geometry("400x600")
newWindow.title("Notepad")
newWindow.config(bg = "white")
top = Frame(newWindow)
top.pack(padx = 10, pady = 5, anchor = 'nw')

b1 = Button(newWindow, text="Open", bg = "white", command = openFile)
b1.pack(in_ = top, side=LEFT)

b2 = Button(newWindow, text="Save", bg = "white", command = saveFile)
b2.pack(in_ = top, side=LEFT)

b3 = Button(newWindow, text="Clear", bg = "white", command = clearFile)
b3.pack(in_ = top, side=LEFT)

b4 = Button(newWindow, text="Exit", bg = "white", command = exit)
b4.pack(in_ = top, side=LEFT)

entry = Text(newWindow, wrap = WORD, bg = "#F9DDA4", font = ("poppins", 15))
entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)

newWindow.mainloop()