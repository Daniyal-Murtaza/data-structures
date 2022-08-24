from tkinter import *
from tkinter.filedialog import *
import tkinter as tk

root = Tk()
root.title("MANAGEMENT")
root.geometry("2000x2000")

# List of Students:
label_1 = Label(root, text="List of Students:",width=0,font=("times new roman", 20))
label_1.place(x=0,y=0)

Button(root, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black').place(x=0,y = 40)

# Grade List:
label_2 = Label(root, text="Grade List:",width=0,font=("times new roman", 20))
label_2.place(x=1,y=150)

Button(root, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black').place(x=0,y = 190)

#--------------

def openNewWindow_Freshman1():

    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(root)
    
    # update grade
    label_08 = Label(newWindow, text="UPDATE GRADE",width=0,font=("times new roman", 40,"bold"))
    label_08.place(x=470,y=10)   
    
    # student name
    label_09 = Label(newWindow, text="Student name:",width=0,font=("times new roman", 20))
    label_09.place(x=0,y=150)   
    
    textBox1 = Entry(newWindow, width = 20, font = ("times new roman", 20))
    textBox1.place(x = 180, y = 150)     
    
    # test 1:
    label_05 = Label(newWindow, text="Test 1:",width=0,font=("times new roman", 20))
    label_05.place(x=0,y=270)   
    
    textBox2 = Entry(newWindow, width = 7, font = ("times new roman", 20))
    textBox2.place(x = 100, y = 270)
    
    # test 2:
    label_04 = Label(newWindow, text="Test 2:",width=0,font=("times new roman", 20))
    label_04.place(x=0,y=370)   
    
    textBox3 = Entry(newWindow, width = 7, font = ("times new roman", 20))
    textBox3.place(x = 100, y = 370)
    
    # test 3:
    label_07 = Label(newWindow, text="Test 3:",width=0,font=("times new roman", 20))
    label_07.place(x=0,y=470)   
    
    textBox6 = Entry(newWindow, width = 7, font = ("times new roman", 20))
    textBox6.place(x = 100, y = 470)
    
    # update button
    Button(newWindow, text='Update',width=15, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = openNewWindow_Freshman1).place(x=0,y = 570)

    # newWindow = tk.Tk()
    newWindow.geometry("40000x60000")
    newWindow.title("Update Grade")
    # newWindow.config(bg = "white")
    top = Frame(newWindow)
    top.pack(padx = 10, pady = 5, anchor = 'nw')


# Upgrade grade:
label_3 = Label(root, text="Update Grade:",width=0,font=("times new roman", 20))
label_3.place(x=2,y=300)

Button(root, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = openNewWindow_Freshman1).place(x=0,y = 340)

# Student Progress
label_4 = Label(root, text="Student Progress:",width=0,font=("times new roman", 20))
label_4.place(x=3,y=450)

Button(root, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black').place(x=0,y = 490)

# Notepad Calling:

def openNewWindow_Freshman():

    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(root)
    
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

    # newWindow = tk.Tk()
    newWindow.geometry("400x600")
    newWindow.title("Notepad")
    # newWindow.config(bg = "white")
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
  
    # A Label widget to show in toplevel
    Label(newWindow, 
          text ="This is a new window").pack()
    
    

# Announcement Pad:
label_5 = Label(root, text="Announcement PAD:",width=0,font=("times new roman", 20))
label_5.place(x=4,y=590)

Button(root, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = openNewWindow_Freshman).place(x=0,y = 640)

root.mainloop()























