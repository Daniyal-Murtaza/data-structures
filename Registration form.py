from tkinter import *

root = Tk()
root.geometry('600x600')
root.title("Update Student Record")

label_0 = Label(root, text="Update Student Record",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Name:",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Father's name:",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Student ID:",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

entry_2 = Entry(root)
entry_2.place(x=240,y=230)

label_4 = Label(root, text="Major:",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

entry_2 = Entry(root)
entry_2.place(x=240,y=280)

label_5 = Label(root, text="Course:",width=20,font=("bold", 10))
label_5.place(x=70,y=330)

entry_2 = Entry(root)
entry_2.place(x=240,y=330)

label_5 = Label(root, text = "Phone No:", width =20, font=("bold", 10))
label_5.place(x=70,y=380)

entry_2 = Entry(root)
entry_2.place(x=240,y=380)

label_5 = Label(root, text = "Address:", width =20, font=("bold", 10))
label_5.place(x=70,y=380)

entry_2 = Entry(root)
entry_2.place(x=240,y=380)

Button(root, text='Submit',width=20,bg='red',fg='white').place(x=180,y = 430)
root.mainloop()























