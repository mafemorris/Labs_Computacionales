import numpy as np
import matplotlib.pylab as plt

#Punto 1
N=[60, 70, 70, 80, 90, 110, 90, 80, 60, 55, 60]
x=np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5])

def Dk(xk,A,B,n0=5,x0=np.array([0]*11),w=5):
    return n0*(A*np.exp(-(xk-x0)**2/(2*w**2))+B)

def poisson(N,D):
    return D**N* np.exp(-1*D)/np.math.factorial(N)
#D es la media de los datos
#N es en ese caso

plt.hist(N,5)

A=np.linspace(0,4,11)
B=np.linspace(0,4,11)

X, Y = np.meshgrid(A, B)
vector= []
for i in range(len(N)):
    a = 1
    for j in range(len(N)):
        a *= poisson(N[j],Dk(x,X,Y)[i])
    vector.append(a)
Z = vector
plt.figure()
plt.contour(X,Y,Z)

#Punto 2
xk = [-5.2, -3.1, -2.8, -3.5] 
def prob(xk,alpha, beta=1):
    prob11= 1
    for i in range(len(xk)):
        prob11 *= beta/(np.pi*(beta**2 + (xk[i] - alpha)**2))
    return prob11


def vector(alpha):
    vect = []
    for i in range(len(alpha)):
        a=prob(xk,alpha[i])*(1/(alpha[-1]-alpha[0]))
        vect.append(a)
    return vect

alpha = np.linspace(0,10,10000)
#N = 10000
#lista = [np.random.random()*np.pi]
#sigma_delta = 1.0

#for i in range(1,N):
 #   propuesta  = [lista[i-1] + sigma_delta * (np.random.random()-0.5)]
  #  r = min(1,vector(propuesta)/vector(lista[i-1]))
   # alpha = np.random.random()
    #if(alpha<r):
     #   lista.append(propuesta)
    #else:
      #  lista.append(lista[i-1])


#alpha = lista
plt.hist(alpha)

plt.figure()
plt.plot(alpha,vector(alpha))
plt.xlabel(r'Lighthouse position $\alpha$ (km)')
plt.ylabel(r'prob($\alpha|\{x_k\},\beta,I$)')
plt.yticks([])


