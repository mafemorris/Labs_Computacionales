from numpy import *
from matplotlib.pylab import *

t = linspace(0,2*pi-(2*pi/32),32)

def par(t,w):
    return 3*cos(w*t) + 2*cos(3*w*t) + cos(5*w*t)

anpar = [3,2,1]
npar = [1,3,5] #para el resto es 0

def impar(t,w):
    return sin(w*t) + 2*sin(3*w*t) + 3*sin(5*w*t)

animpar = [1,2,3]
nimpar = [1,3,5]

def mixed(t,w):
    return 5*sin(w*t) + 2*cos(3*w*t) + sin(5*w*t)

anmix = [5,2,1]
nmix = [1,3,5]


def xk(lista):
    N=len(lista)
    lis = [0]*N
    for k in range(N):
        suma = 0
        for n in range(N):
            suma += exp(-2*pi*1j*n*k/N)*lista[n]
        lis[k]=abs(suma)
    return array(lis)/N

figure(figsize=(15,15))

subplot(3,2,1)
plot(t,par(t,1),'o')
title('par puntos') 
subplot(3,2,2)
title('par fourier') 
stem(xk(par(t,1)))


subplot(3,2,3)
plot(t,impar(t,1),'o')
title('impar puntos') 
subplot(3,2,4)
title('impar fourier') 
stem(xk(impar(t,1)))

subplot(3,2,5)
plot(t,mixed(t,1),'o')
title('mixed puntos') 
subplot(3,2,6)
title('mixed fourier')
stem(xk(mixed(t,1)))

savefig('1.png')

t1 = t
y1 = lambda t: 5 + 10*sin(t+2)
y2 = lambda t: 10*sin(t+2)
y3 = lambda t: 5 + 10*sin(t)
y4 = lambda t: 10*sin(t)
figure(figsize=(15,15))
subplot(4,2,1)
plot(t1,y1(t1),'o',label='5 + 10 sin(t+2)')
legend()
subplot(4,2,2)
stem(xk(y1(t1)))
subplot(4,2,3)
plot(t1,y2(t1),'o',label='10 sin(t+2)')
legend()
subplot(4,2,4)
stem(xk(y2(t1)))
subplot(4,2,5)
plot(t,y3(t),'o',label='5 + 10 sin(t)')
legend()
subplot(4,2,6)
stem(xk(y3(t)))
subplot(4,2,7)
plot(t,y4(t),'o',label='10 sin(t)')
legend()
subplot(4,2,8)
stem(xk(y4(t)))
savefig('2.png')




t = linspace(0,1 -(1/32) ,32)
t1 = linspace(0,4 -(4/32) ,32)
alia = lambda t: sin(pi*t/2) + sin(2*pi*t)
alia1 = lambda t: sin(pi*t/2)
alia2 = lambda t: sin(2*pi*t)
figure(figsize=(15,15))
subplot(3,2,1)
plot(t1,alia(t1))
subplot(3,2,2)
stem(xk(alia(t1)))
subplot(3,2,3)
plot(t1,alia1(t1))
subplot(3,2,4)
stem(xk(alia1(t1)))
subplot(3,2,5)
plot(t,alia2(t))
subplot(3,2,6)
stem(xk(alia2(t)))
savefig('3.png')