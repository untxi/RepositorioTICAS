from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("200x200")

frame = ttk.Frame(root, width=80, height=45)
frame['borderwidth'] = 8
frame['padding'] = (5,10)
frame['relief'] = 'ridge'
frame.pack()
l = Label(root, text="Starting ...")
l.pack()
frame.bind('<Enter>',
           lambda e: l.configure(text='Moved mouse inside'))
frame.bind('<Leave>',
           lambda e: l.configure(text='Moved mouse outside'))
frame.bind('<1>',
           lambda e: l.configure(text='Clicked left mouse button'))
frame.bind('<Double-1>',
           lambda e: l.configure(text='Double clicked'))
frame.bind('<B1-Motion>',
           lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
root.mainloop()

