from tkinter import *

root = Tk()
root.geometry('500x330')
root.title("FORGOT  PASSWORD?")
root.resizable(False,False)

label_0 = Label(root, text="FORGOT PASSWORD?",width=20,font=("times new roman", 23))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Enter your ID",width=20,font=("times new roman", 12))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Enter your Code",width=20,font=("times new roman", 12))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

Button(root, text='Submit',width=17,bg='red',fg='white').place(x=180,y = 240)
root.mainloop()























