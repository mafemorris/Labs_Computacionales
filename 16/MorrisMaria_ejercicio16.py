import numpy as np
from numpy import *
from numpy.linalg import *
import matplotlib.pylab as plt

datos = np.loadtxt('numeros_6.txt')
x = np.array([1]+[i[0] for i in datos])
y = np.array([1]+[i[1] for i in datos])
grad = 4
c = np.zeros(grad+1)
num = 300
J = np.zeros(num)
alpha = 0.01
def funcion(x,y,c):
    return sum(((h(x,c) - y)**2)/(2*len(x))) #para verificar si esta bien

def h(x,c):
    a = [c[i]*x**i for i in range(len(c))]
    b = np.zeros(len(x))
    for i in range(len(a)):
        for j in range(len(a[i])):
            b[j] += a[i][j]
    return b

def grad(x,y,alpha,c,num):
    for i in range(num):
        for j in range(len(c)):
            c[j] -= (alpha/len(x))*(h(x,c)-y).dot(x)
        J[i] = funcion(x,y,c)
    return c,J

            
c,J = grad(x,y,alpha,c,num)
plt.plot(np.arange(len(J)),J)
plt.figure()
plt.scatter(x,y)
inx = np.linspace(min(x)-0.2,max(x)+0.2,100)
iny = h(inx,c)
plt.plot(inx,iny)


datos = np.loadtxt('numeros_20.txt')
grad = 4
x = np.array([[1]+[i[0] for i in datos] for i in range(grad)])
y = np.array([1]+[i[1] for i in datos])
c = np.zeros(grad+1)
alpha = 0.1
def grad(x,y,alpha,c,num):
    c = pinv(x.transpose().dot(x)).dot(x.transpose()).transpose()*y
    return c
def fun(x,c):
    c=c[0]
    a = [c[i]*x**i for i in range(len(c))]
    b = np.zeros(len(x))
    for i in range(len(a)):
        for j in range(len(a[i])):
            b[j] += a[i][j]
    return b
c = grad(x,y,alpha,c,num)
plt.figure()
plt.scatter(x[0],y)
inx = np.linspace(min(x[0])-0.2,max(x[0])+0.2,100)
iny = fun(inx,c)
plt.plot(inx,iny)
plt.show()