import numpy as np
import matplotlib.pylab as plt

#Punto 1
def MB(x,sigma):
    return x**2 * np.exp(-(x**2)/(2*sigma**2))
x=np.linspace(0,40,100)
sigmas = [1,2,10]
plt.figure()
for i in sigmas:
    plt.loglog(x,MB(x,i))
plt.title('MB')
plt.xlabel('x')
plt.ylabel('MB')
plt.savefig('mb.png')

#Punto 2
sigma = np.arange(2,20)
def gaussian(df,sigma,N,a=1):
    yi, wi = np.polynomial.legendre.leggauss(N)
    xi = (sigma/2)*((1+yi)/(1-yi))
    dw = ((2*(sigma/2))/(1-yi**2))*wi
    df1 = dw*df(xi,sigma) 
    integ = sum(df1)
    return integ
inte = []
plt.figure()
for i in range(len(sigma)):
    inte.append(gaussian(MB,sigma[i],100))
plt.loglog(sigma,inte)
plt.title('Integral')
plt.xlabel('Sigma')
plt.ylabel('IntegralGauss')
plt.savefig('mb_int.png')

#Punto 3
def central(f,t,h):
    return (f(MB,t+h,100)-f(MB,t-h,100))/(2*h)
deri = []
plt.figure()
for i in range(len(sigma)):
    deri.append(central(gaussian,sigma[i],0.003))
plt.loglog(sigma,deri)
plt.title('Derivada')
plt.xlabel('Sigma')
plt.ylabel('Dervada Central')
plt.savefig('mb_int_prime.png')