from tkinter import *
class Registration_from:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Update Student Record")
        bg_color = "#074463"
        title = Label(self.root, text = "Update Student Record" , bd=12, relief = GROOVE , bg=bg_color, fg="white", font = ("times new roman", 30, "bold"), pady = 2).pack(fill = X)

        
        cname_lbl = Label(self.root, text = "Name", font=("times new roman", 15, "bold"))
        cname_lbl.place(x=0, y=80, relwidth=1)
        
        cname_text = Entry(cname_lbl, width= 20, font = "arial 15").grid(row=0, column=1, pady = 5, padx = 10)
        
root = Tk()
obj = Registration_from(root)
root.mainloop()