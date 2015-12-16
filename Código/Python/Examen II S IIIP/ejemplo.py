from MatDispersa import *

m = MatDispersa(50, 50)
m.asigna(20, 10, 8)
m.asigna(20, 4, 71)
m.asigna(20, 30, 6.2)
m.asigna(20, 35, 3)
m.asigna(20, 41, 9)
m.asigna(20, 49, 8)
m.asigna(5, 3, 6)

t = MatDispersa(80, 30)
t.asigna(5, 3, 4)
t.asigna(6,0, 8)
            
print("Matriz_1")
print(m)
print("Matriz_2")
print(t)
s = MatDispersa(1000, 2000)
valores = "12140307\n99\n2371"
s.carga(30, 8, valores, 2)
print("Matriz_3")
print(s)
print("Densidad = %9.5f" % s.densidad())
print("Matriz 4 = Matriz_1 + Matriz_2")
print(m + t)
print("Matriz 5 = Matriz_3 + 4")
print(s + 4)
        



            
            


