import numpy as np
import matplotlib.pyplot as plt

#Ejercicio 1.1
b = np.random.rand(4,8)
b[:,-1] = -1
b[:,1] = 2
print(b)

#Ejercicio 1.2
a = np.random.normal(size=100)
print( a[a>2.0])

#Ejercicio 1.3
a=np.random.normal(size=1000)
b=np.sign(a)
print('Se cambio de {} a {}'.format(a,b))

#Ejercicio 4.1
plt.figure(figsize=(10,10))
a = np.linspace(0,10,200)
x = np.cos(5*a)
y = np.sin(4*a)
plt.plot(x,y)
plt.show()

#Ejercicio 4.2
fig = plt.figure()
r = np.linspace(0,1)
a=plt.subplot(1,2,1)
def generator(n):
    theta = np.random.random(n)*2*np.pi 
    return np.sin(theta), np.cos(theta)

x,y = generator(1000)
x,y = np.outer(r,x), np.outer(r,y)
a.scatter(x, y)

b=plt.subplot(1,2,2)
def gene3D(n):
    theta = np.random.uniform(0,2*np.pi,n)
    phi = np.random.uniform(0,np.pi,n)
    return np.sin(phi)*np.cos(theta), np.sin(phi)*np.sin(theta), np.cos(phi)
x,y,z = gene3D(1000)

b.scatter(x,y,z)
plt.show()

#Ejercicio en clase
def y(t,vy):
    return vy*t -(1/2)*10*t**2
def x(t,v0):
    return v0*t
for i in np.linspace(-19,19,20):
    vy=np.sqrt(20**2-i**2)
    t=np.linspace(0,2*vy/10)
    plt.plot(x(t,i),y(t,vy),c='black')
    plt.scatter(x(t,i)[np.argmax(y(t,vy))],np.max(y(t,vy)),c='r')
plt.savefig('grafica.pdf')
plt.show()
