import numpy as np
import matplotlib.pylab as plt

def aIntegrar(xs): #funcion que se quiere integrar (x1+x2+..+x10)**2
    return sum(xs)**2

N=[2]
for i in range(1,13):
    N.append(2*N[i-1]) #sample sizes
    
def montecarlo(N, aIntegrar=aIntegrar, MH=0, g=1, d=10):
    if MH==0:
        MH = [np.random.random() for i in range(d)] #10 es la cantidad de variables a integrar
    b = [(1/N)*aIntegrar(MH) for i in range(N)]
    return sum(b)*g

analitica = 155/6 #valor de la integral analitica

monte=[]
for i in N:
    a = [montecarlo(i) for j in range(16)]
    monte.append(np.mean(a))
monte=np.array(monte)

print('analitica',analitica,'montecarlo',monte)

error = (analitica-monte)/analitica

print('error',error)

#N=1/np.sqrt(N)

#plt.figure()
#plt.plot(N,error)
#plt.figure()
#plt.loglog(N,error)



#Gaussian
def gaussian(df,N,a=1,b=0):
    yi, wi=np.polynomial.legendre.leggauss(N)
    xi = (yi/(1-yi**2))
    dw = ((1+yi**2)/(1-yi)**2)*wi
    df1 = dw*df(xi) 
    integ = sum(df1)
    return integ
def newMontecarlo(N, f, g, a, d=10): 
    b = [(1/N)*f(i) for i in a]
    return sum(b)

def f(x):
    return np.cos(x)
def g(x):
    return np.exp(-x**2-x)
def df(x):
    return f(x)*g(x)
def MH(g,N):
    lista = [np.random.random()*np.pi]
    sigma_delta = 1.0

    for i in range(1,N):
        propuesta  = lista[i-1] + sigma_delta * (np.random.random()-0.5)
        r = min(1,g(propuesta)/g(lista[i-1]))
        alpha = np.random.random()
        if(alpha<r):
            lista.append(propuesta)
        else:
            lista.append(lista[i-1])
    return lista

N=5000
#Punto 1
print('Cuad Gausseana 1: {}'.format(gaussian(df,20)))
#punto 2
print('se demora, por lo que no esta a 10**5')
print('Montecarlo con N={} da {}: '.format(N,newMontecarlo(N,f,g,MH(g,N))*gaussian(g,N)))


def gd(r):
    return np.exp(-r)
def fd(r):
    return np.cos(np.sqrt(r))

def montecarlo(N, aIntegrar=aIntegrar, MH=0, g=1, d=10, a=np.ones(1), b=np.zeros(1)):
    MH = MH(gd,d) #10 es la cantidad de variables a integrar
    b = [(1/N)*aIntegrar(sum(np.array(MH)**2)) for i in range(N)]
    return sum(b)*g

print('La integral de montecarlo para N={} en 2 dimensiones es de: {} '.format(N, montecarlo(N,aIntegrar=fd,MH=MH,d=2,g=gaussian(gd,N))))

m = int(input('ingrese numero'))
print('La integral de montecarlo para N={} en {} dimensiones es de: {} '.format(N,m,montecarlo(N,aIntegrar=fd,MH=MH,d=2,g=gaussian(gd,N))))

