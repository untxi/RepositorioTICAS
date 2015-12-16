## Clase 5
## Programa utilizando divisiones
## PROGRAMA : Suma extrema igual al medio

def sumed(num):
    print(True) if isinstance (num,int) and 99 < num < 1000 and num // 100 + num % 10 == num // 10 % 10 else print(False)
     

## Clase 6
## Primer programa utilizando un if
## PROGRAMA : F(X)

def f(x):
    print("0") if x < 10 else print(x**2+2)

## Clase 6
## Segundo programa utilizando if's
## PROGRAMA : G(X)

def g(x):
    if x <= 0: print (x)
    elif 0 < x < 1000: print( x**3 - 1)
    else: print( x**2 - x + 2)

###############################################################################
## PROGRAMA    : Calculo de Impuestos
## AUTOR       : Luis Rojas Alfaro
## FECHA       : 7/08/2014
## DESCRIPCIÓN : Programa que asigna la cantidad a pagar dependiendo del
##               impuestos por provincia
##
## ENTRADAS    : Provincia de origen, edad y cantidad de dinero
## SALIDAS     : Cantidad a pagar por concepto de impuestos
## RESTRICCION : Origen es tira, edad es entero y cantidad es numérico.
###############################################################################  

def calcimp():
    ## Cuando se tienen problemas por que el ususario ha tecleado tildes:
        ##string.replace
    print("--> CALCULADORA DE IMPUESTOS\n--> Versión BETA1.0 por AVAS\n")
    origen   = input("Digite la provincia................: ")
    edad     = input("Digite su edad ....................: ")
    cantidad = input("Digite la cantidad a pagar.........: ")
    origen = origen.replace("é","e")
    origen = origen.replace ("ó","o")
    origen = origen.strip()
    origen = origen.lower()
    
    assert cantidad.strip() != ["."] and cantidad.strip()!= "." and cantidad.strip("0123456789 ")in [".",""], "Cantidad no Válida"
    assert edad.strip() != "" and edad.strip("0123456789 ") == "", "Edad no Válida"

    edad     = int(edad)
    cantidad = float (cantidad)
    if origen in ("san jose", "cartago", "puntarenas", "limon", "guanacaste", "heredia", "alajuela"):
        if origen == "san jose":
            print (cantidad * 0.10) if (edad) <= 25 else print(cantidad * 0.15)
        if origen in  ("alajuela", "cartago"):
            print (cantidad * 0.05) if (edad) <= 20 else print(cantidad * 0.12)
        if origen in ("puntarenas", "limon", "guanacaste"):
            print (cantidad * 0.08) if (edad) <= 30 else print(cantidad * 0.13)
        if origen == "heredia":print ("No paga impuestos")
    else:assert False, "Provincia Invalida o Desconocida"
calcimp()


