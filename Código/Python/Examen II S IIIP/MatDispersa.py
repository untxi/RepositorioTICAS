##########################################
##
## Instituto Tecnológico de Costa Rica
## Escuela de Computación
## Introducción a la Programación
## III Parcial - II semestre 2014
##
## Estudiante : Luis Rojas Alfaro
##
##########################################

class MatDispersaError(Exception):
    pass

class MatDispersa:
    """ Implementa una matriz dispersa.
        Se mantienen los siguientes atributos:
            filas    - cantidad de filas
            columnas - cantidad de columnas
            matriz   - un diccionario que contiene como llaves
                       la posición del elemento y como valor el
                       el valor de la matriz en esa entrada.
    """
    
    _largo_separador = 20

    @staticmethod
    def posicionValida(i,j, m, n):
        """ Retorna True si la posición i,j es válida en una
            matriz de m filas y n columnas, bajo el supuesto
            que las filas y las columnas se numeran a partir
            de 0.
            Entradas :
                i - fila
                j - columna
                m - número de filas
                n - número de columnas
            Salidas:
                True si (i, j) es una posición
                válida en la matriz, de otra
                forma retorna False
        """
        return type(i) == int and type(j) == int and \
           0 <= i < m and \
           0 <= i < n

    def __init__(self, filas = 100, columnas = 100):
        """Metodo constructor de la Clase. Asignación de los parametros iniciales"""

        self.filas = filas
        self.columnas = columnas
        self.dictio={}


    def validoValor(self):
        l = []
        for x in self.dictio:
            if float(self.dictio[x]) in [0.0,0] :
                l.append(x)

        for x in l:
            del self.dictio[x]
        
        return self.dictio
        

        
    def densidad(self):
        """ Muestra la cantidad porcentual de unos asociados a una matriz
            dispersa con respecto a su contenido total
        """

        return (len(self.dictio) /(self.filas * self.columnas)) * 100


    def asigna(self, i, j, valor):
        """ Retorna el valor en la posición i,j de la matriz.
            Entradas :
                i - fila.
                j - columna.
                valor - valor que se desea en la posicion
            Restricciones :
                i, j son posiciones válidas en la matriz.
                       
        """
        if not MatDispersa.posicionValida(i,j, self.filas, self.columnas):
            raise MatDispersaError("Referencia fuera de rango")

        if (i,j) in self.dictio and valor in [0,0.0]:
            del self.dictio[i,j]

        else:
            self.dictio[i,j]= float(valor)

        self.dictio = MatDispersa.validoValor(self)

    


    def valor(self, i, j):
        """Retorna el valor correspondiente a la posicion seleccionada"""
        
        if not (i in range(self.filas) or j in range(self.columnas)):
            raise MatDispersaError("Los parametros son invalidos")

        return self.dictio.get((i, j), 0)



    def carga(self, di, dj, tira, ancho = 1):
        """ Permite una asignación multiple de valores a la Matriz Dispersa mediante el
            uso de una tira con valores numericos y cuya dimension sin el \n es multiplo
            del ancho
        """
        

        if not (di in range(self.filas) or dj in range(self.columnas)):
            raise MatDispersaError("Los parametros son invalidos")

        if tira != str and ancho <= 0:
            raise MatDispersaError("Los parametros son invalidos")
            
        l=[]
        while len (tira):
            if tira[0] != "\n":
                l.append(tira[0:ancho])
                tira = tira[ancho:]
            else:
                l.append(" ")
                tira = tira[1:]

        fila   = di
        column = dj
        i      = 0
        while i < len(l):
            
            if l[i] != " ":
                self.dictio[fila,column] = float(l[i])
                column +=1
            else:
                fila   +=1
                column  = dj
            i+=1

        self.dictio = MatDispersa.validoValor(self)
        return self.dictio
            

    def __add__(self, v):
        """ Permite la suma de dos matrices o la suma de una matriz y un numero
            ya sea flotanto o entero.

            Entrada: V - Valor a sumar o Matriz
            Salida : Sumada - Matriz con la suma
            Restricción: Valor solo puede ser nmerico o MatDispersa
        """

        if type(v) == int or type(v) == float:
            sumada = MatDispersa(self.filas,self.columnas)
            for x in range (self.filas):
                for y in range (self.columnas):
                    if (x,y) in self.dictio:
                        sumada.dictio[x,y] = float(self.dictio[x,y]) + v
                    else:
                        sumada.dictio[x,y] = v
            sumada.dictio = MatDispersa.validoValor(self)
            return sumada
                        

        elif type(v) == MatDispersa:
            
            sumada = MatDispersa(self.filas,self.columnas)

            for x in range (self.filas):
                for y in range (self.columnas):
                    sumada.dictio[x,y] = float(self.dictio.get((x,y),0)) + float(v.dictio.get((x,y),0))

            sumada.dictio = MatDispersa.validoValor(self)
            return sumada
  

        else:
            raise MatDispersaError("No se pueden sumar los parametros")
             


    def __repr__(self):
        """ Retorna un string con la representación de la matriz.
            Entradas :
                Ninguna.
            Salidas  :
                Tira con la representación de la matriz.
        """

        ancho = max(len(str(self.filas)),
                     len(str(self.columnas)))

        ## Obtiene una lista ordenada de las posiciones (i,j)
        ## de la matriz que tienen valores
        llaves = sorted(self.dictio.keys())

        ## Produce el encabezado de la salida, el cual contiene
        ## el número de filas y columnas de la matriz.
        salida = "=" * MatDispersa._largo_separador + \
                 "\n:: Filas    -> %s\n:: Columnas -> %s\n" % \
                 (str(self.filas).zfill(ancho),
                  str(self.columnas).zfill(ancho)) + \
                  "=" * MatDispersa._largo_separador
        
        filaAnterior = None
        cuantos = 1
        
        for x in llaves:  ## Para todas las entradas de la matriz

            if x[0] != filaAnterior: ## Hay un cambio de fila
                
                salida += "\n-: Fila %s  | " % str(x[0]).zfill(ancho) + \
                          "(%d, %d) = %.1f" % (x[0], x[1], self.dictio[x])
                filaAnterior= x[0]
                cuantos = 1
                
            else:
                
                if cuantos == 4: ## Por línea imprime máximo 4 entradas
                    cuantos = 1
                    salida += "\n-:      %s  | (%d, %d) = %.1f" % \
                              (" " * ancho, x[0],
                               x[1], self.dictio[x])
                
                else: 
                    salida += ", (%d, %d) = %.1f" % (x[0],
                                                     x[1], float(self.dictio[x]))
                    cuantos += 1

        return salida + "\n" + "=" * MatDispersa._largo_separador


            
            


