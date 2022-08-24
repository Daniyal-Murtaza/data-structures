from tkinter import *
from PIL import ImageTk, Image

root = Tk()

canvas = Canvas(root, width = 300 ,height = 160)
image = ImageTk.PhotoImage(Image.open("C:\\Users\\HU-Student\\Desktop\\login\\images\\image.jpg"))

canvas.create_image(0,0,anchor = NW, image = image)
canvas.pack()

root.mainloop()