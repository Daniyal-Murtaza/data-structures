from tkinter import *
from tkinter import messagebox

# from PIL import ImageTk, Image
window = Tk()

canvas = Canvas(window, width = 3000 ,height = 169900)
# image = ImageTk.PhotoImage(Image.open("C:\\Users\\Syed Hussain\\Desktop\\New folder (2)\\hh.jpg"))

# canvas.create_image(0,0,anchor = NW, image = image)
canvas.pack()

window.resizable(False,False)
window.geometry("800x500+300+100")
window.title("Login")

def openNewWindow_Freshman():
    def check():
        code = "9876"
        password = "ad+1000"
        verify = code1.get()
        if (verify == code):
            label1 = Label(newWindow, text = " Your password is: "+password+"       " ,fg = "black", font = ("new times roman", 17, "bold"))
            label1.place(x = 240, y = 300) 
            
        else:
            label1 = Label(newWindow, text = " Verification code is incorrect! ", fg = "black", font = ("new times roman", 17, "bold"))
            label1.place(x = 240, y = 300)

#-------------------------------------------------------------------------------------------------------------------------------------            
            
    newWindow = Toplevel(window)
    newWindow.resizable(False,False)
    newWindow.geometry("800x500+300+100")
    
    label1 = Label(newWindow, text = " If you want to retrieve the Password then write your verification code here! ", fg = "black", font = ("new times roman", 16, "italic"))
    label1.place(x = 0, y = 15)
        
    label1 = Label(newWindow, text = " Verification Code ", fg = "black", bg = "yellow" , font = ("times new roman", 20, "bold"))
    label1.place(x = 300, y = 110)
    
    button2 = Button(newWindow, text = "   Check   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = check)
    button2.place(x = 350, y = 210)   
        
    code1 = StringVar()
    textBox2 = Entry(newWindow, textvar = code1, width = 15, font = ("arial", 20, "bold"))
    textBox2.place(x = 300, y = 160)
    
#----------------------------------------------------------------------------------------------------------------------------------

def login():
    users = {'admin': 'ad+1000'}
    username = userName.get()
    Pass = password.get()
    if username in users :
        if (users[username] == Pass):
            label4 = Label(window, text = ("Welcome " + username),width = 25, font = ("arial", 40, "bold"))
            label4.place(x = 0, y = 400)
                                        
        else:
            label4 = Label(window, text = ("Incorrect Password for " + username),width = 25, font = ("arial", 40, "bold"))
            label4.place(x = 0, y = 400)

    else:
        label4 = Label(window, text = (username + " does not exist"),width = 25, font = ("arial", 40, "bold"))
        label4.place(x = 0, y = 400)

#----------------------------------------------------------------------------------------------------------------

label1 = Label(window, text = " Login System ", fg = "black", font = ("new times roman", 40, "bold"))
label1.place(x = 200, y = 15)

label2 = Label(window, text = "User Name :", font = ("arial", 16, "bold"))
label2.place(x = 110, y = 150)

userName = StringVar()
textBox1 = Entry(window, textvar = userName, width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 290, y = 150)

label3 = Label(window, text = "Password :", font = ("arial", 16, "bold"))
label3.place(x = 116, y = 250)

password = StringVar()
textBox2 = Entry(window, textvar = password, width = 30, font = ("arial", 16, "bold"))
textBox2.place(x = 290, y = 250)

button1 = Button(window, text = "   Login   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = login)
button1.place(x = 230, y = 340)

button1 = Button(window, text = "   Forgot Password?   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = openNewWindow_Freshman)
button1.place(x = 360, y = 340)
         
#display window
window.mainloop()