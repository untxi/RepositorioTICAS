###
# 20 de Noviembre del 2014 .|||.
# Luis Rojas Alfaro
# Introducción a la Programación
# IV Examen Parcial
###

class EstError(Exception):
    pass

class Est():

    def __init__(self, arch):
        """ Inicializador de la clase Estadistica """
        
        ## Apertura del archivo
        self.arch = arch

        try:
            apertura  = open(self.arch+".txt")
        except:
            raise EstError("No existe este archivo")
                
        self.txt  = apertura.readlines()
        self.paises    = {"504":"Honduras","505":"Nicaragua","506":"Costa Rica","507":"Panamá"}

        def Revisa(dictio):
            """ Retorna True si toda la información es válida """
            return      all([type(dictio["Nombre"]) == str,
                        type(int(dictio["Sexo"])) == int and int(dictio["Sexo"]) in [0,1],
                        type(int(dictio["Nacionalidad"])) == int and int(dictio["Nacionalidad"]) in [504,505,506,507],
                        type(int(dictio["Edad"])) == int])

        ## Crea el diccionario con información y revisa si los
        ## datos estan completos y correctos
        self.personal, self.errores = [], []
        for x in self.txt:
            info = {"Nombre": x[0:14],
                    "Sexo" : x[15],
                    "Nacionalidad":x[16:19],
                    "Edad":x[19:21]}
            
            ## Se crea una lista con los datos erroneos
            if x[21:] not in ["","\n"] or Revisa(info) == False:
                self.errores.append(info)

            else:
                self.personal.append(info)

        ## Avisa de los errores al usuario
        if len(self.errores) != 0: print("Algunos archivos no se cargaron a memoria")

    def __repr__(self):
        """ Crea la representación de la información """
        decor = "==" * 48 + "\n" + 44 * " " + "Personal"+ "\n" + "==" * 48 + "\n"
        salida = decor + "\n"

        for x in self.personal:
            salida += "Nombre: "+ str(x["Nombre"]) + "\n"
            salida += "Sexo: "+ ("Masc" if int(x["Sexo"])== 0 else "Fem") + "\n"
            salida += "Nacionalidad: "+ self.paises[str(x["Nacionalidad"])] + "\n"
            salida += "Edad: "+ str(x["Edad"]) + "\n" + "==" * 48 + "\n"

        return (salida)


    def datos(self):
        """ Permite eaminar algunas generalidades y hace estadistica:
            n = cantidad de linea
            e = cantidad errores
            p = cantidad datos cargados
            h, m = cantidad de hombres y mujeres
            ed = promedio de edades
        """
        
        n = len(self.errores) + len(self.personal)
        e = len(self.errores)
        p = len(self.personal)
        h,m,ed = 0,0,0
        for x in self.personal:
            if x["Sexo"] == "0": h+=1
            else: m+=1
            ed+= int(x["Edad"])

        return (n,e,p,h,m,ed / len(self.personal))


    def reporte_sexo_país(self, sexo, pais):
        """ Permite presentar información sobre algunos generos en los países
        """

        if sexo not in [0,1,2]: raise EstError("No existe tal Sexo")
        
        ## Segun el código; retrna el país al que pertenece la persona
        tpais, marca = [],[]
        for x in self.paises:
            tpais.append(self.paises[x])
            marca.append(x)

        if pais in tpais:
            GPS = marca[tpais.index(pais)]
        else:
            EstError("No operamos ese pais")


        if sexo in [0,1]:
            for x in self.personal:
                if int(x["Sexo"]) == sexo and x["Nacionalidad"] == GPS:
                    print(x)

        elif sexo == 2:
            for x in self.personal:
                if x["Nacionalidad"] == GPS:
                    print(x)


    def distribucion(self):
        ListaPaisana = []
        m, f = 0, 0
        for x in self.paises:
            for y in self.personal:
                if x == y["Nacionalidad"]:
                    if int(y["Sexo"]) == 0:m+=1
                    else:f+=1
            ListaPaisana.append ((self.paises[x],{"Hombres": m,
                                                  "Mujeres": f,
                                                  "Total":m+f}))
            m, f = 0, 0


        ## proyectando la salida

        decor = "==" * 48 + "\n" + 44 * " " + "DISTRIBUCIÓN"+ "\n" + "==" * 48 + "\n"
        
        salida  = decor + "\n"
        salida += "País          " + 17*" " + "H " + 17*" " + "  M" + 17*" " + " Total" + "\n"
        totalm, totalf, totalT = 0, 0, 0
        for x in ListaPaisana:
            general = 11 - len(str(x[0]))
            totalm += int(x[1]["Hombres"])
            totalf += int(x[1]["Mujeres"])
            totalT += int(x[1]["Total"])
            salida += (str(x[0]) + " " * general + 20*" " +  str(x[1]["Hombres"]) + 20*" " +
                        str(x[1]["Mujeres"]) + 20*" " +  str(x[1]["Total"]) + "\n" )
                    
        salida += "TOTAL" + 6 * " " + 20*" " +  str(totalm) + 20*" "  + str(totalf) + 20*" " + str(totalT) + "\n" 

        print (salida +"\n"+ "=*" * 48)
