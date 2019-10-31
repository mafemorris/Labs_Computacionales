#Hice funciones con los métodos con el fin de no volver a repetirlos, sino utiliazando lo que ya había hecho en vista de que no se podían utilizar otros métodos. 

#Ejercicio 1
m = [5,3,2,8,1,4,9,1,2,4]
def fun(x):
    for i in range(len(x)):
        if not (x[i]%2==0):
            for j in range(len(x)):
                if not (x[j]%2==0):
                    a=x[j]
                    if(x[i]<x[j]):
                        x[j]=x[i]
                        x[i]=a
    return x
print(fun(m)) 

#Ejercicio 2
b = [5,3,5,1,26,7,2,4,33,9,2,3,4]
pares=[]
impares=[]

def f1(pares, impares, x):
    for i in x:
        if(i%2==0):
            pares.append(i)
        else:
            impares.append(i)

def orden(n, q):
    x= [] + n
    for i in range(len(x)):
        for j in range(len(x)):
            a=x[j]
            if(x[i]<x[j]):
                x[j]=x[i]
                x[i]=a
    x = x[::q]
    return x

f1(pares, impares, b)
print('De la lista {}, los pares son {}, en orden descendiente {}, los impares son {}, en orden ascendente {}.'.format(b,pares,orden(pares,-1), impares, orden(impares,1)))

#Ejercicio 3
a = [1,3,2,6,7,36,95,23,4,90,78,5,0]
b = [3,6,4,6,85,13,6,9,2,3,5,80,5,6,5]
a,b,c = [],[],orden(a+b,1)
f1(a,b,c)
a=a[::-1]
def inter(a,b,c):
    for j in range(0,len(c),2):
        c[j]=a[int(j/2)]
    for j in range(1,len(c),2):
        c[j]=b[int((j-1)/2)]
    return(c)
print(inter(a,b,c))

#Ejercicio 4
a = [1,5,6,9,2]
b = [0,12,5,2,3]
a,b,c = [],[],orden(a+b,1)
i=0
while (i<len(c)):
    j=i+1
    while (j<len(c)):
        if(c[i]==c[j]):
            c.pop(j)
            j-=1 #permanezca en la misma casilla y se pueda volver a revisar si hay más iguales.
        j+=1
    i+=1
f1(a,b,c)
a=a[::-1]
print(inter(a,b,c))