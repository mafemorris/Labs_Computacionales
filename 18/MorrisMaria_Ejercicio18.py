from numpy import *
from numpy.linalg import *
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt

#Arrestos

data = pd.read_csv('USArrests.csv') #Importa datos
states = array(data['Unnamed: 0']) #Nombres estados
murder = array(data['Murder']).reshape(50,1) #asesinatos
murder = (murder - murder.mean())/std(murder) #normalizar
assault = array(data['Assault']).reshape(50,1) #atraco
assault = (assault - assault.mean())/std(assault) #normalizar atraco
upop = array(data['UrbanPop']).reshape(50,1) #Urban pop
upop = (upop - upop.mean())/std(upop) #normalizar Urban Pop
rape = array(data['Rape']).reshape(50,1) #violacion
rape = (rape - rape.mean())/std(rape) #normalizar violacion

X = column_stack((murder,assault,upop,rape)) #Juntar los features
Sigma = cov(X.T) #matriz de covarianza de los features
u,s,v= svd(Sigma) #da los vectores propios u
ured = u[:,:2] #toma solo los primeros dos para la reduccion de dimension
z = X.dot(ured) #multiplicacion con los features para tener los componentes principales z
z1,z2 = z[:,0], z[:,1] #separar cada componente

plt.figure(figsize=(8,9))
plt.scatter(-z1,-z2,s=s) #como son vectores propios describen el espacio y se pueden multiplicar, en este caso por -1
mpl.rcParams['text.color'] = 'tab:blue' #cambia el color de la letra a azul
for i in range(len(z1)):
    plt.text(-z1[i],-z2[i],states[i]) #grafica los nombres de los estados por punto
crimen = ['Murder','Assault','UrbanPop','Rape'] #nombre de los atributos que se estan evaluando
mpl.rcParams['text.color'] = 'darkorange' #cambia el color de la letra para las flechas a naranja
for i in range(4):
    plt.arrow(0,0,-u[i][0],-u[i][1],length_includes_head=True, head_width=.05, color = 'darkorange') #hace las flechas
    plt.text(-u[i][0]+0.1,-u[i][1]-0.15,crimen[i]) #Hay que multiplicarlos por 3 para que sean mas visibles y queden como la imagen. 
plt.plot(linspace(-3,3,100),zeros(100),':',c='gainsboro') #grafica una linea sobre el eje x
plt.plot(zeros(100),linspace(-3,3,100),':',c='gainsboro') #grafica una linea sobre el eje y
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.savefig('arrestos.png')


#Carros 

data = pd.read_csv('Cars93.csv')
model = array(data['Model'])
HP = array(data['Horsepower']).reshape(93,1)
HP = (HP - HP.mean())/std(HP)
length = array(data['Length']).reshape(93,1)
length = (length - length.mean())/std(length)
wi = array(data['Width']).reshape(93,1)
wi = (wi - wi.mean())/std(wi)
ftc = array(data['Fuel.tank.capacity']).reshape(93,1)
ftc = (ftc - ftc.mean())/std(ftc)
X = column_stack((HP,length,wi,ftc))
Sigma = cov(X.T)
u,s,v= svd(Sigma)
ured = u[:,:2]
z = X.dot(ured)
z1,z2 = z[:,0], z[:,1]
plt.figure(figsize=(9,7))
plt.scatter(-z1,-z2,s=s)
mpl.rcParams['text.color'] = 'tab:blue'
for i in range(len(z1)):
    plt.text(-z1[i],-z2[i],model[i])
flecha = ['Horse Power','Length','Width','FTC']
mpl.rcParams['text.color'] = 'darkorange'
for i in range(4):
    plt.arrow(0,0,-u[i][0],-u[i][1],length_includes_head=True, head_width=.05, color = 'darkorange')
    plt.text(-u[i][0]+0.1,-u[i][1]-0.15,flecha[i]) 
plt.plot(linspace(-3,3,100),zeros(100),':',c='gainsboro')
plt.plot(zeros(100),linspace(-2,2,100),':',c='gainsboro')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.tick_params(axis='both',top=True,right=True)
plt.savefig('carros.png')