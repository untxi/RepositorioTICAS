#########################################################################
##                                                                     ##
## Instituto Tecnológico de Costa Rica.                                ##
## Escuela de Computación.                                             ##
## Taller de Programación.                                             ##
##                                                                     ##
## II semestre de 2014.                                                ##
##                                                                     ##
## Examen Parcial                                                      ##
## Profesor: Juan C. Gómez P.                                          ##
##                                                                     ##
## Programa Base.                                                      ##
##                                                                     ##
#########################################################################


from turtle import TurtleScreen, RawTurtle, TK

class SnakeError(Exception): pass

class Snake():
    """ Implementa un Snake que puede moverse en una 
        cuadrícula imaginaria dede m filas por n columnas.
        Las filas y columnas se numeran a partir de 1.
        El snake tendrá una largo, que incluye su cabeza.
        El largo tiene que ser mayor que 1.
        La cabeza se pinta de un color y los segmentos de
        su cuerpo en otro.
        El snake se puede mover en forma horizontal o
        vertical.
        Para mover el snake se utilizan las flechas
        direccionales y la tecla "x" (que también mueve
        el snake hacia abajo).
    """

    ## Atributos de clase que definen el tamaño por
    ## defecto de la cuadrícula.
    FILAS = 40
    COLUMNAS = 30

    ## Atributos de clase que define el tamaño (en pixeles)
    ## de cada elemento de la cuadrícula.
    DIM = 10

    ## Atributo de clase que defifne el tamaño por
    ## defecto del snake.
    LARGO_SNAKE = 4

    ## Atributos de clase que define a partir de que
    ## coordenadas en el eje horizontal(x) y vertical(y)
    ## se empieza a dibujar la cuadrícula.
    DY = 20
    DX = 20

    @staticmethod
    def deme_posicion(i,j):
        """ Retorna la posicion superior izquierda en eje x, eje y
            de un elemento i,j en la cuadrícula imaginaria.
            Entradas:
                i     : Fila en la cuadrícula imaginaria.
                j     : Columna en la cuadrícula imaginaria.
            Salidas:
                (x,y) : Posición de la esquina superior izquierda
                        en donde se encuentra la entrada (i,j)
            Supuesto:
                (i,j) es una posición válida en la cuadrícula
                      imaginaria.
        """
        x = Snake.DX + (j - 1) * (Snake.DIM + 1)
        y = Snake.DY + (i - 1) * (Snake.DIM + 1)
        return (x, y)
    

    def __init__(self, filas = FILAS, columnas = COLUMNAS,
                 largo = LARGO_SNAKE):
        """Crea la culebra y su cuadrícula.
            Entradas:
                filas    : # de filas en la cuadrícula imaginaria.
                columnas : # de columna en la cuadrícula imaginaria.
                largo    : Tamaño del snake incluyendo la cabeza.
            Salidas:
                Snake en una cuadrícula según las dimensiones indicadas.
            Supuesto:
                La ventana, según las dimensiones establecidas,
                cabe en la ventana.
                El snake cabe en la cuadrícula.

        """

        ## Funciones locales al constructor ##
        
        def segmento(color, i, j):
            """ Dibuja un segmento del snake en posicion i, j con el color
                indicado.
            Entradas:
                color : Color del segmento a dibujar.
                (i,j) : Ubicación en que se desea dibujar el
                        segmento en la cuadrícula imaginaria.
            Salidas:
                Dibujo del segemento con el color indicado en
                la posición (i,j) de la cuadrícula imaginaria.
            Supuesto:
                El color es uno válido en Tkinter.
                (i,j) es una posición válida en la
                cuadrícula imaginaria.
            """

            ## Determina la posición en los ejes
            ## reales de la posición (i,j) de la
            ## cuadrícula imaginaria.
            x, y = Snake.deme_posicion(i, j)

            ## Prepara el lápiz para dibujar
            ## un rectánculo relleno.
            self.lapiz.fillcolor(color)
            self.lapiz.pu()
            self.lapiz.setpos(x, y)
            self.lapiz.seth(0)
            self.lapiz.pd()
            self.lapiz.begin_fill()

            ## Dibuja el rectángulo con 4
            ## movimientos !!!
            for i in range(4):
                self.lapiz.fd(Snake.DIM+1)
                self.lapiz.left(90)

            ## Cierra el relleno.
            self.lapiz.end_fill()

        def mueva_snake(direccion):
            """ Mueve el snake en la dirección indicada.
            Entradas:
                direccion : Dirección en que se mueve el snake.
            Salidas:
                Actualización del snkae en pantalla.
                Si el snake pega contra un borde o contra ella
                misma no avanza.
            Supuesto:
                dirección es alguno de los valores 
                "Up", "Down", "Left" o "Right".
            """

            ## Obtiene la posición actual de la cabeza del snake.

            ci, cj = self.snake[-1][0], self.snake[-1][1]
            
            ## Calcula la nueva posición de la cabeza según
            ## la dirección indicada por el usuario.

            if direccion == "Up":
                i, j = (ci if ci == 1 else ci - 1, cj)
            elif direccion == "Down":
                i, j = (ci if ci == self.filas else ci + 1, cj)
            elif direccion == "Left":
                i, j = (ci, cj if cj == 1 else cj - 1)
            elif direccion == "Right":
                i, j = (ci, cj if cj == self.columnas else cj + 1)

         
            if not((i,j) in self.snake): ## se asegura que el snake
                                         ## no choque contra sí mismo !!

                self.scr.tracer(False) 

                ## Borra la cola. La cola está en la
                ## posición 0 de la lista self.snake.

                segmento("white", self.snake[0][0], self.snake[0][1])
                del self.snake[0]

                ## Pinta la antigua cabeza de color azul para que sea
                ## parte del cuerpo.  La cabeza es el último elemento
                ## de la lista self.snake.

                segmento("blue", self.snake[-1][0], self.snake[-1][1])

                ## Agrega la nueva cabeza.  La cabeza nueva cabeza
                ## se agrega al final de la lista. 

                self.snake.append((i, j))
                segmento("red", i, j)

                self.scr.tracer(True)
                
        def dibuja_horizontales():
            """ Dibuja las filas+1 lineas horizontales.
            Entradas:
                Ninguna.
            Salidas:
                Dibujo de las líneas horizontales de la
                cuadrícula imaginaria en que se moverá el
                snake.
            """
            
            dy = Snake.DY ## Posición en eje y de la primera 
                          ## línea horizontal.

            ## Calcula la posición en eje x en que finalizan
            ## todas la líneas horizontales.
            
            posFin_x = Snake.DX + self.columnas * (Snake.DIM + 1)

            for i in range(self.filas+1):
                self.lapiz.up()
                self.lapiz.setpos(Snake.DX, dy)
                self.lapiz.down()
                self.lapiz.setpos(posFin_x, dy)
                dy += Snake.DIM + 1

        def dibuja_verticales():
            """ Dibuja las columnas+1 lineas verticales 
            Entradas:
                Ninguna.
            Salidas:
                Dibujo de las líneas verticales de la
                cuadrícula imaginaria en que se moverá el
                snake.
            """

            dx = Snake.DX ## Posición en eje x de la primera
                          ## línea vertical.

            ## Calcula la posición en eje y en que finalizan
            ## todas la líneas verticales.
            
            posFin_y = Snake.DY + self.filas * (Snake.DIM + 1)
            for j in range(self.columnas+1):
                self.lapiz.up()
                self.lapiz.setpos(dx,Snake.DY)
                self.lapiz.down()
                self.lapiz.setpos(dx, posFin_y)
                dx += Snake.DIM + 1

        def dibuja_escenario():
            """ Dibuja la cuadrícula y el snake: el cuerpo en azul y la
                cabeza en rojo.
            Entradas:
                Ninguna.
            Salidas:
                Dibujo de la cuadrícula imaginaria en que se moverá el
                snake.
            """

            self.scr.tracer(False)

            ## Dibuja la cuadricula
            dibuja_horizontales()
            dibuja_verticales()

            ## Dibuja el cuerpo del snake
            for x in self.snake[:-1]:
                segmento("blue",x[0],x[1])

            ## Dibuja la cabeza
            segmento("red", self.snake[-1][0], self.snake[-1][1])    

            self.scr.tracer(True)

        ############################################################    
        ## Inicio de las instrucciones del constructor __init__.  ##
        ############################################################

        ## Verifica restricciones, sino se cumplen dispara un
        ## SnakeError.
        if not (isinstance(filas,int) and isinstance(columnas,int) and \
           isinstance(largo,int)):
            raise SnakeError("Type Error")
        else:
            
            ## Guarda las dimensiones de la cuadrícula
            ## imaginaria y del snake en atributos de instancia.
            self.filas = filas
            self.columnas = columnas
            self.largo = largo

            ## Crea la ventana y estable un título para la misma.
            self.root = TK.Tk()
            self.root.title("Snake v1.0 / 2014")

            ## Obtiene la posición (x,y) en la ventana de la 
            ## última fila y columna de la cuadrícula imaginaria,
            ## lo anterior con el objetivo de establecer el
            ## tamaño de la ventana.
            x, y = Snake.deme_posicion(filas, columnas)

            ## Calcula el ancho y el alto de la ventana
            anchoVentana = x + Snake.DX + Snake.DIM + 1
            altoVentana  = y + Snake.DY + Snake.DIM + 1

            ## Crea un área de dibujo (canvas) con un ancho y
            ## alto que está en función de la cuadrícula
            ## en que se moverá el snake.
            
            self.canvas = TK.Canvas(self.root, width=anchoVentana,
                                    height=altoVentana)
            self.canvas.pack()

            ## Crea un área de dibujo para tortugas.
            self.scr = TurtleScreen(self.canvas)

            ## Establece un sistema de coordenadas en donde
            ## el punto (0,0) se ubica en la esquina superior
            ## izquierda.
            ## El eje x va de 0 a positivos de izquierda a derecha.
            ## El eje y va de 0 a positivos de arriba hacia abajo.
            self.scr.setworldcoordinates(0,altoVentana,anchoVentana,0)
            self.scr.reset()

            ## Crea la tortuga para dibujar
            self.lapiz = RawTurtle(self.scr)
            self.lapiz.ht()

            ## Crea el snake.
            ## El snake corresponde a una lista de pares
            ## ordenados (x, y) en donde cada uno de estos
            ## elementos corresponde a un segmento del snake.
            ## La cabeza del snake se ubica en la última
            ## posición de la lista.
            ## El snake creado queda en posición horizontal
            ## y su cabeza mira hacia la derecha.  La cola
            ## se ubica en la posición 1,1. Observe que se
            ## utilizaron listas por comprensión para
            ## construir el snake.  En este punto el snake
            ## no es visible.
            
            self.snake = [(1,eje_y) for eje_y in range(1, self.largo + 1)]

            ## Dibuja la cuadrícula y el snake.
            dibuja_escenario()

            ## Establece el binding entre las teclas para el movimiento
            ## del snake y las funciones que atenderán dicho movimiento.
            ## En todos los casos se utiliza la misma función solo que
            ## el parámetro con que se invoca es diferente.
            
            self.scr.onkeypress(lambda : mueva_snake("Up"), "Up")       # Arriba
            self.scr.onkeypress(lambda : mueva_snake("Right"), "Right") # Derecha
            self.scr.onkeypress(lambda : mueva_snake("Down"), "Down")   # Abajo
            self.scr.onkeypress(lambda : mueva_snake("Left"), "Left")   # Izquierda
            self.scr.onkeypress(lambda : mueva_snake("Down"), "x")      # Otra vez abajo

            ## Se queda escuchando los eventos.
            ## El programa termina cuando el usuario cierre la ventana.
            self.scr.listen()

if __name__ == '__main__':
    Snake(12,10,3).root.mainloop()
