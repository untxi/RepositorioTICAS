from tkinter import *

class Application(Frame):

    def __init__(self, master=None):
        self.root = master
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def say_hi(self):
        print("Hola !")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Salir"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.root.destroy

        self.QUIT.pack({"side" : "left"})

        self.hi_there = Button(self, text = "Diga hola",
                               fg = "blue",
                               command = self.say_hi)
        self.hi_there.pack(side = "left")


root = Tk()
app = Application(master=root)
app.mainloop()

    
        
