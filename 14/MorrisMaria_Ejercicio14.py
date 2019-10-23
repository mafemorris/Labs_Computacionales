import numpy as np
import matplotlib.pylab as plt

def f(E,V=10):
    m = np.sqrt(V-E)
    return (m*np.tan(m) - np.sqrt(E))
E = np.linspace(0,9,100)
plt.plot(E,f(E))
plt.axhline(linewidth=1,color='r')
plt.title('TAN')
plt.show()

#El cero esta cerca de 8 y cerca de 0.
eps = 10**-6
xp1 = 9
xn1 = 7.5
xp0 = 0
xn0 = 0.5
def bisection(f,xp,xn):
    while True:
        x = (xp+xn)/2
        if f(xp)*f(x) > 0:
            xp = x
        else:
            xn = x
        if np.abs(f(x))< eps:
            return x,f(x)


def fequi(E):
    m = np.sqrt(10-E)
    return (np.sqrt(E)*(np.cos(m)/np.sin(m)) - m)
plt.figure()
plt.plot(E,fequi(E))
plt.axhline(linewidth=1,color='r')
plt.title('COT')
plt.show()

a0, fa0=bisection(f,xp0,xn0)
a1, fa1=bisection(f,xp1,xn1)
b1, fb1=bisection(fequi,xp1,xn1)
print('Los 0s de la funcion estan en {} y en {}. La funcion es equivalente ya que los 0s son iguales, en {}.'.format(a0,a1,b1))

def NR(f,x,dx,V=10):
    while True:
        F=f(x,V)
        if(np.abs(F)<= eps):
            return x
        m=dx
        while (f(x+m,V))**2 > (f(x,V))**2:
            m/=2
        df=(f(x+m,V)-f(x-m,V))/dx
        dx=-F/df
        x += dx
print('Por el metodo de Newton Raphson el valor de la derivada es {}'.format(NR(f,8,0.01)))

xs = [2.031331588946557076e+00,5.886777538940683563e+00,2.195744759275823021e+00,6.821886748452244298e+00,8.793952398085184141e-01,2.951577398416659559e+00,4.454332895499525158e+00,-1.804396045394615955e+00,-5.841925974092386120e+00,-1.113495627653518838e+00]
sigma = np.linspace(1,7,100)
A=1/9
eps = 10**-7
def P(x,sigma):
    return (1/(2*np.pi*sigma**2)) * np.exp(-(x**2)/(2*sigma**2))
def L(P,x,sigma):
    a = [P(i,sigma) for i in x]
    m = np.prod(a)*A
    return m
li = [L(P,xs,i) for i in sigma]
plt.plot(sigma,li)

def central(f,xs,sigma,h):
    return (f(P,xs,sigma+h)-f(P,xs,sigma-h))/(2*h)

c=[central(L,xs,i,0.01) for i in sigma]
plt.plot(sigma,c)

plt.show()

def NR(central,sig,xs,dsig,h):
    while True:
        F=central(L,xs,sig,h)
        if(np.abs(F)<= eps):
            return sig
        m=dsig
        while (central(L,xs,sig+m,h))**2 > (central(L,xs,sig,h))**2:
            m/=2
        df=(central(L,xs,sig+m,h)-central(L,xs,sig-m,h))/dsig
        dsig=-F/df
        sig += dsig
print('el sigma0 esta en {}'.format(NR(central,3,xs,0.01,0.01)))