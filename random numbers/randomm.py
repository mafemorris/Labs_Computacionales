import numpy as np
import matplotlib.pylab as plt
import random

#Punto 1-2, Funcion hecha con recursividad que genera los datos aleatorios hechos con el metodo
lista = []
def generador(r1,a,c,m,l):
    if (len(l)>=m):
        return(l)
    ri = (a*r1+c)%m
    l.append(ri)
    return generador(ri,a,c,m,l)
generador(10,57,1,256,lista)
print('La lista generada es: {}'.format(lista))
#Se repite cada M por lo que si se varía el M el periodo va a ser cada M.

#Punto 3, se separa la función anterior entre los pares e impares.
x = lista[1::2]
y = lista[::2]
plt.subplot(2,2,1)
plt.plot(x,y,'o')

#Punto 4
plt.subplot(2,2,2)
plt.plot(range(0,256),lista)

#Punto 5.
ran =np.random.random(2**3)
plt.subplot(2,2,4)
plt.plot(range(2**3),ran)

plt.subplot(2,2,3)
plt.plot(ran[1::2],ran[::2],'o')

plt.savefig('random.png')


#Punto6
lisi=[]
lisi=generador(90,100,int('B',16),2**3,lisi)
print(lisi,len(lisi))
lisi= np.array(lisi)/(2**3)
plt.plot(range(2**3),ran)
plt.plot(range(2**3),lisi,'r')
plt.savefig('randompy.png')
#Punto prueba

def prueba(k, N, li):
    lisk = li**k
    return np.sqrt(N)*np.abs((1/N)*sum(li) - (1/(k+1)))
k=[1,3,7]
N=[100,10000]

def diferencia(k,N):
    listaBuena = np.random.random(N)
    aB = []
    for i in k:
        for j in N:
            listaMala = np.array(lista[:j])/256
            aB.append(prueba(i,j,listaBuena)-prueba(i,j,listaMala))
    return aB
diferencia(k,N)
        