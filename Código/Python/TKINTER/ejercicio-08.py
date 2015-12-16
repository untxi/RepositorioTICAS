from tkinter import *
from tkinter import ttk

def hexfill(v):
    assert isinstance(v,int) and 0 <= v < 256
    hexa = hex(v)
    if len(hexa) == 3:
        return "0"+hexa[2:]
    else:
        return hexa[2:]

def toHex(r,g,b):
    return "#"+hexfill(r)+hexfill(g)+hexfill(b)

root = Tk()


cr = ttk.Label(root)
mapa = PhotoImage(file=r'costarica.gif')
root.geometry("%dx%d" %(mapa.width(), mapa.height()+50))
cr['image'] = mapa
cr.pack()
nombre = ttk.Label(root)
nombre["text"] = "Costa Rica"
nombre["foreground"]=toHex(255,13,13)

nombre.pack()
root.mainloop()

