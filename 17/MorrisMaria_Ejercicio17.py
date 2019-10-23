import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import *
from numpy.linalg import *

data = pd.read_csv('Cars93.csv')

HP = np.array(data['Horsepower']).reshape(93,1)
HP = (HP-HP.mean())/(HP.max()-HP.min())
price = np.array(data['Price']).reshape(93,1)
price = (price-price.mean())/(price.max()-price.min())
X = np.column_stack((price,HP))
Sigma = cov(X.T)
u,s,v= svd(Sigma)
ured = u[0]

z1 = ured[1]*(HP-np.mean(HP))+ured[0]*(price-np.mean(price)) #first principal component

z2 = ured[0]*(HP-np.mean(HP))- ured[1]*(price-np.mean(price)) #second principal component



plt.figure()
plt.scatter(price,HP)
plt.plot([ured[0]*0.5,-ured[0]], [ured[1]*0.5,-ured[1]],'r')
plt.plot([-u[1][0]*0.3,u[1][0]*0.3], [-u[1][1]*0.3,u[1][1]*0.3],'g')
plt.xlabel('Price')
plt.ylabel('HP')
plt.savefig('primera.png')

plt.figure()
plt.plot(z1,z2,'ro')
plt.plot(np.linspace(-1,1,100),np.zeros(100))
plt.plot(z1,np.zeros(len(z1)),'gx')
plt.xlabel('first principal component')
plt.ylabel('second principal component')
plt.savefig('segunda.png')
plt.show()
