import numpy as np
import matplotlib.pylab as plt
import random
#Algo 1.1
def direct_pi(N): #pi para niños
    Nh=0
    for i in range(N):
        x=random.random()*random.choice((-1,1))
        y=random.random()*random.choice((-1,1))
        if(x**2+y**2 <1):
            Nh+=1
    return Nh
print(direct_pi(10))

#Algo 1.2
def markov_pi(N): #pi para adultos
    Nh=0
    x,y=1,1
    for i in range(N):
        dX = random.random()*random.choice((-1,1))
        dy = random.random()*random.choice((-1,1))
        if (np.abs(x+dX)<1 and np.abs(y+dy)<1):
            x+=dX
            y+=dy
        if (x**2 +y**2 <1):
            Nh+=1
    return Nh
markov_pi(10)

def pi(v):
    if(v==0):
        return 0.3
    if(v==1):
        return 0.7
    
#Algo 1.8
def markov_two_site(k): #Donde k es un numero entre 0 y 1
    l=0
    if(k==0):
        l=1
    gamma = pi(l)/pi(k)
    if(random.random()<gamma):
        k=l
    return k
a=[markov_two_site(random.choice((0,1))) for i in range(20)]
print(a)

def f(x,sigma=1,):
    y = (1/(np.sqrt(2*sigma**2*np.pi)))*np.exp(-(x)**2/(2*sigma**2))
    return y

#Algo 1.18
def gauss(sigma):
    phi = np.random.random(1000)*2*np.pi
    gamma = -np.log(np.random.random(1000))
    r=sigma*np.square(2*gamma)
    x=r*np.cos(phi)
    y=r*np.sin(phi)
    return x,y
x,y=gauss(1)
print(x.mean())
x.sort()
plt.hist(x,bins=100,density=True)
plt.plot(np.linspace(-5,5),f(np.linspace(-5,5)))
plt.show()