from tkinter import * 
import tkinter

from PIL import ImageTk, Image


raiz = tkinter.Tk()

raiz.geometry("500x300")
boton1 = tkinter.Button(raiz, text = "click")
boton1.pack()

#raiz.iconbitmap("py")
raiz.config(bg = "red")



miFrame = Frame()
miFrame.pack(side ="left")
miFrame.config(bg="green")
miFrame.config(width="150", height="100")

#img = ImageTk.PhotoImage(Image.open("test_image.jpg"))  
#l=Label(image=img)
#l.pack()

raiz.mainloop()


