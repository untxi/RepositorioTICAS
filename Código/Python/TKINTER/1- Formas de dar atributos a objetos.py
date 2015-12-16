from tkinter import *

##root = Tk()
##root.title("Hola")
##
##w = Label(root,
##          text="Hola Clase como están ... esto es un ejemplo de tkinter", bg="blue", fg="white")
##w.pack()
##
##root.mainloop()

##Segunda forma

root = Tk()
root.title("Hola")

w = Label(root)
w["text"]= "Hola Clase como están ... esto es un ejemplo de tkinter"
w["bg"]  = "blue"
w["fg"]  = "white"
w.pack()

root.mainloop()
