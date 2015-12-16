#######################################################################################################################
#DESCRIPCIÓN: Verifica que un numero entero convertido a base 2 tenga los digitos alternados (010101).
#             Pruebese con: 10, 170 -> True
#######################################################################################################################


def alternado(n):
    esperado = n % 2
    while n and n % 2 == esperado:
        esperado = (esperado+1) % 2 ## Comparar contra si mismo
        n//=2                       ## 2 % 2 = 0
    return n==0
    
##################################################################################
## Descripción: Leer 5 números, obtener su promedio y determinar cuál es el más
##              cercano al promedio. Por ejemplo para 10, 8, 14, 2, 3 el promedio
##              es 7.4, por lo tanto el más cercano es 8.
##################################################################################

def cercano(a,b,c,x,y):
    prom = (a + b + c + x + y) // 5
    l = [a,b,c,x,y]
    myr, i = max(l), 0
    
    while i < len(l):
        if abs(l[i] - prom) < abs(myr - prom): ## Comparar contra uno
            myr = l[i]
        i+=1
    print("Promedio: ",prom, " Cercano: ", myr)

##################################################################################
## Descripción: Leer 5 números, obtener su promedio y determinar cuál es el más
##              cercano al promedio. Por ejemplo para 10, 8, 14, 2, 3 el promedio
##              es 7.4, por lo tanto el más cercano es 8.
##################################################################################

def sumafibo(inicio, fin): ## 2 a 5 = 1+2+3+5
    i, a, b, suma = 0, 0, 1, 0
    while i < fin:
        a, b, i = a + b, a, i + 1
        suma += a if i >= inicio else 0  # Poner codiciones en el sumador
    print(suma)                          # para sumar hasta donde se desea
