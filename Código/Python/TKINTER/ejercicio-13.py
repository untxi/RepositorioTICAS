from tkinter import *

## Ejemplo de como mover con el mouse un objeto dibujado
## sobre un canvas.

class Test(Frame):

    ## Especificación de acciones a ejecutar por eventos.
    def iniciaMovimiento(self, event):
        # Recuerda la posición de inicio del objeto a mover
        self.lastx = event.x
        self.lasty = event.y

    def mueveRaton(self, event):
        # Mueve el ratón.
        self.draw.move(CURRENT, event.x - self.lastx, event.y - self.lasty)
        self.lastx = event.x
        self.lasty = event.y
            

    def ingreso(self, event):
        # Cambia el color cuando el mouse ingresa al objeto (enter).
        self.draw.itemconfig(CURRENT, fill="red")

    def salida(self, event):
        # Cambia el color cuando el mouse sale del objeto (leave).
        self.draw.itemconfig(CURRENT, fill="blue")

    def createWidgets(self):
        # Crea los widgets de la ventana.

        # Crea el canvas
        self.draw = Canvas(self, width="5i", height="5i")
        self.draw.pack(side=LEFT)

        # Crea el ratón - objeto a mover.
        fred = self.draw.create_oval(10, 10, 30, 30,
                                     fill="green", tags="selected")

        # Realiza el bind de eventos que permiten cambiar el color
        # del ratón cuando el mouse ingresa o sale de él.
        self.draw.tag_bind(fred, "<Any-Enter>", self.ingreso)
        self.draw.tag_bind(fred, "<Any-Leave>", self.salida)

        # Realiza el bind de eventos que permiten mover el ratón
        Widget.bind(self.draw, "<1>", self.iniciaMovimiento)
        Widget.bind(self.draw, "<B1-Motion>", self.mueveRaton)
        

    def __init__(self, master=None):
        # Constructor

        # La clase es una subclase de Frame.
        # Con Frame.__init__ se realiza la instanciación de
        # atributos; lo anterior implica la creación de la
        # ventana.
        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()

test = Test()
test.mainloop()
