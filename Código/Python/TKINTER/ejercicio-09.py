from tkinter import *
from tkinter import ttk
from random import choice

def cambie():
    l.configure(text="Aleatorio %d" % choice(range(10)))

root = Tk()
root.geometry("200x200")

l = ttk.Label(root, text="hola Mundo.....")
b = ttk.Button(root, text="Cambiar", command = cambie)
#b.state(['disabled']) 
l.pack()
b.pack()
root.mainloop()

