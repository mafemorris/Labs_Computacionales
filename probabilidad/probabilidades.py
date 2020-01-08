import numpy as np
import random
#Punto 1
def prob(N):
    a = [0]*N
    med = 0
    for i in np.arange(N*2):
        b = round(random.random()*(N-1))
        a[b]+=1
        if(a[b]==2):
            med = i+1
            break
    return(med)
media = 0
for i in range(10000):
    media += prob(10)
media/=10000
print('La cantidad de medias en promedio que debe sacar para obtener un par es de {}'.format(round(media)))

#Punto 2
def probCC(N):
    a = [0,0]
    med = 0
    for i in np.arange(N):
        b = round(random.random())
        a[b]+=1
    if(a[0]==N/2):
        med=1
    return(med)
media = 0
for i in range(10000):
    media += probCC(100)
media/=10000
print('La probabilida de que sean 50 cara y 50 sello es de {}'.format(media))

#Punto 3
def probCumple(N):
    a = [0]*365
    med = 0
    for i in np.arange(N):
        b = round(random.random()*(365-1))
        a[b]+=1
        if(a[b]==2):
            med=1
            break
    return(med)
def calc(p):
    media = 0
    j=0
    while(media<=p):
        for i in range(1000):
            media += probCumple(j)
        media/=1000
        j+=1
    return (j,media)
a,b = calc(0.5)
c,d = calc(0.9)
print('La cantidad minima de personas que se necesita para que dos personas tengan el mismo cumpleaños es de {} con una probabilidad de {}, y de {} para una probabilidad de {}'.format(a,b,c,d))