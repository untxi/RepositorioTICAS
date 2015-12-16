from tkinter import *
from tkinter import ttk

#def enEntrada(e):
#    print("Se ha detectado el evento Mouse Enter : ", e.x, e.y)
#    l.configure(text='El mouse entro en la etiqueta...')

root = Tk()
root.geometry("200x200")
l =ttk.Label(root, text="Starting...")
l.grid()
l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside in %d,%d' % (e.x,e.y)))
l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
l.bind('<1>', lambda e: l.configure(text='Clicked left mouse button'))
l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
l.bind('<B1-Motion>', lambda e:
       l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
root.mainloop()

