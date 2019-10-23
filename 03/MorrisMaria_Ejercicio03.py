import random
#Ejercicio 1.1
points = 0
amount = 0
while points < 100:
    points += random.randint(1,6)
    amount += 1
print('La cantidad de veces que se tiro el dado es de {}, para un total de {} puntos.'.format(amount,points))

#Ejercicio 2.1
import math
a, b = [0,1,2], [2,3,4]
c, d = [0,0], [1,1]
e, f = [1,5], [2,2]
def distance (a,b):
    suma = 0
    for i in range(len(a)):
        suma += (a[i] - b[i])**2
    return math.sqrt(suma)
print('Para las posiciones {} y {} es de {}. \nPara las posiciones {} y {} es de {}. \nPara las posiciones {} y {} es de {}.'.format(a,b,distance(a,b),c,d,distance(c,d),e,f,distance(e,f)))

#Ejercicio 3.1 
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius #all attributes must be preceded by "self."
    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius
a = input('Ingrese el radio del circulo:')
circulo = Circle(float(a))
print(circulo.perimeter())

#Ejercicio 3.2
class Vector3D:
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z 
    def dot(self, c):
        return ((self.x * c.x) + (self.y * c.y) + (self.z * c.z))
    def cross(self, c): #punto 2 trabajo en clase
        a, b, d = (self.y*c.z - self.z*c.y), (-1*(self.x*c.z - self.z*c.x)), (self.x*c.y - self.y*c.x)
        self.x, self.y, self.z = a, b, d
v = Vector3D(2, 0, 1)
w = Vector3D(1, -1, 3)
print(v.dot(w))
v.cross(w)
print('El vector resultante es ({},{},{}])'.format(v.x,v.y,v.z))


#Ejercicio 4.1
import random
lista = [i for i in range(10)]
print('Lista antes {}'.format(lista))
random.shuffle(lista)
print('Lista despues {}'.format(lista))


#Segunda parte.
#Funciones
hamlet = open("hamlet.txt")
def cuenta_palabra(archivo, n_letras):
    l = hamlet.read()
    l = l.split()
    veces = 0
    palabra = ''
    for i in l:
        if (len(i)>=n_letras) and (l.count(i)>veces):
            veces=l.count(i)
            palabra=i
    return palabra, veces

p, cuenta = cuenta_palabra("hamlet.txt", n_letras=7)
print("La palabra mas repetida es: {} que se encuentra {} veces\n".format(p, str(cuenta)))