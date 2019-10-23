%pylab
#Punto1
H = np.linspace(0,1,500)
def prob(H,R,N):
    return (H**R)*((1-H)**(N-R)) #R cantidad de caras en N tiros
plt.figure(figsize=(10, 10)) 

a = [1,10,100,1000]
for i in range(len(a)):
    plt.subplot(2,2,i+1)
    if a[i]<3:
        plt.plot(H,prob(H,a[i],a[i]),label=a[i])
    elif a[i]==3:
        plt.plot(H,prob(H,a[i]-1,a[i]),label=a[i])
    else:
        plt.plot(H,prob(H,np.ceil(a[i]*0.3),a[i]),label=a[i])
    plt.xlabel('Bias-weighting for heads H')
    plt.ylabel('prob(H|{data},I)')
    plt.yticks([])
    plt.legend()


#punto 2   
xk = [-5.2, -3.1, -2.8, -3.5] 
def prob(xk,alpha, beta=1):
    prob11= 1
    for i in range(len(xk)):
        prob11 *= beta/(np.pi*(beta**2 + (xk[i] - alpha)**2))
    return prob11

alpha=np.linspace(-5,5,100)
def vector(alpha):
    vect = []
    for i in range(len(alpha)):
        a=prob(xk,alpha[i])*(1/(alpha[-1]-alpha[0]))
        vect.append(a)
    return vect
plt.plot(alpha,vector(alpha))
plt.xlabel(r'Lighthouse position $\alpha$ (km)')
plt.ylabel(r'prob($\alpha|\{x_k\},\beta,I$)')
plt.yticks([])

#punto3

#si fuera solo una
x_i=[0.5, 1.0, 0.8, 0.9] 
def prob(x_i, Q):
    prob11= 1
    for i in range(len(x_i)):
        prob11 *= np.exp(-Q*x_i[i])/Q
    return prob11

Q=np.linspace(0.1,5,100)
def vector(Q):
    vect = []
    for i in range(len(Q)):
        a=prob(x_i,Q[i])*(1/(Q[-1]-Q[0]))
        vect.append(a)
    return vect

plt.figure(figsize=(10, 10)) 
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.plot(Q,vector(Q))
    plt.xlabel('Q')
    plt.ylabel('Probabilidad')
    plt.yticks([])


#para las cuatro
x_i=[0.5, 1.0, 0.8, 0.9] 
def prob(x_i, i, Q):
    prob11 = np.exp(-Q*x_i[i])/Q
    return prob11

plt.figure(figsize=(10, 10)) 
Q=np.linspace(0.1,5,100)
def vector(Q):
    for j in range(len(x_i)):
        vect = []
        for i in range(len(Q)):
            a=vect[i-1]*prob(x_i,j,Q[i])*(1/(5-0.1))
            vect.append(a)
        plt.subplot(2,2,j+1)
        plt.plot(Q,vect)
        plt.xlabel('Q')
        plt.ylabel('Probabilidad')
        plt.yticks([])
    return vect
vector(Q)