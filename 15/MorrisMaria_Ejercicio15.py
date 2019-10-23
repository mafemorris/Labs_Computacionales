import numpy as np
from numpy import *
from numpy.linalg import *
from numpy.linalg import solve
import matplotlib.pylab as plt

A = array([[1,2,3],[22,32,42],[55,66,100]])
b = array([1,2,3])
x = solve(A, b)
print('la direrencia es: ',dot(A,x)-b,x)
dot(inv(A),A)
dot(inv(A),b)

A=array([[4,-2,1],[3,6,-4],[2,1,8]])
Ainv = inv(A)
print('matrices identidades de ambas formas {}'.format(dot(Ainv,A),dot(A,Ainv)))
Ainv2 = (1/263)*np.array([[52,17,2],[-32,30,19],[-9,-8,30]])
print('resta de las marices inversas de ambas formas {}'.format(Ainv-Ainv2))

bs = [[12,-25,32],[4,-10,22],[20,-30,40]]
xs = [solve(A,i) for i in bs]
print('los valores son: x1 = {}, x2 = {}, x3 = {}'.format(xs[0],xs[1],xs[2]))

A = array([[1,2],[-2,1]])
print('los valores propios y los vectores propios son: ',eig(A))

A = array([[-2,2,-3],[2,1,-6],[-1,-2,0]])
x1 = (1/sqrt(6))*array([-1,-2,1])
x2 = (1/sqrt(5))*array([-2,1,0])
x3 = (1/sqrt(10))*array([3,0,1])
a,b=eig(A)
a, b, x2,x1,x3
print('los valores propios y los vectores propios son: {}. con x1 = {}, x2 = {}, x3= {}'.format(b,x2,x1,x3))

n=9
eps=1E-6
der = zeros((n,n),float)
f = zeros((n), float)
x=array([0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,1,1])
def plotfig():
    plt.figure()
    L1 = 3.0
    L2 = 4.0
    L3 = 4.0
    plt.plot([0,L1*x[3]],[0,-L1*x[0]])
    plt.plot([L2*x[3],L2*x[4]],[-L2*x[0],-L2*x[1]])
    plt.plot([L3*x[4],L3*x[5]],[-L3*x[1],L3*x[2]])
    
def F(x,f):
    f[0]=3*x[3] + 4*x[4] + 4*x[5] - 8.0
    f[1]=3*x[0] + 4*x[1] - 4*x[2]
    f[2]=x[6]*x[0]-x[7]*x[1]-10.0
    f[3]=x[6]*x[3]-x[7]*x[4]
    f[4]=x[7]*x[1]+x[8]*x[2]-20.0
    f[5]=x[7]*x[4]-x[8]*x[5]
    f[6]=pow(x[0],2) + pow(x[3],2) -1.0
    f[7]=pow(x[1],2) + pow(x[4],2) -1.0
    f[8]=pow(x[2],2) + pow(x[5],2) -1.0

def dFi_dXi(x, der, n):
    h=1E-4
    for j in range(n):
        temp = x[j]
        x[j] = x[j] + h/2
        F(x,f)
        for i in range(n):
            der[i,j] = f[i]
        x[j] = temp
    for j in range(0,n):
        temp = x[j]
        x[j] = x[j] - h/2
        F(x,f)
        for i in range(n):
            der[i,j]=(der[i,j]-f[i])/h
        x[j] = temp

for a in range(1,100):
    F(x,f)
    dFi_dXi(x,der,n)
    B=array([[-f[0]],[-f[1]],[-f[2]],[-f[3]],[-f[4]],[-f[5]],[-f[6]],[-f[7]],[-f[8]]])
    sol = solve(der,B)
    dx = take(sol,(0, ),1)
    for i in range(n):
        x[i]=x[i]+dx[i]
    errX = 0.0
    errXi = 0.0
    errF = 0.0
    
    if x[i] != 0:
        errXi = abs(dx[i]/x[i])
    else:
        errXi = abs(dx[i])
    if errXi > errX :
        errX = errXi
    if abs(f[i]) > errF:
        errF = abs(f[i])
    if (errX <= eps) and (errF <= eps):
        break
plotfig()

A = array([[1.0/(i+1) for i in range(j,100+j)] for j in range(100)])
b = array([1.0/(i+1) for i in range(100)])
print('------>En el Jupyter notebook si sale el vector de 1 y 0s, pero en la terminal aproxima como si el determinante fuera 0.')
x=solve(A,b)
print(x)