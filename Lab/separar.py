archivo = open("datos.data",'r')
archivo = list(archivo)
archivo = [i.split(',') for i in archivo]
def cambiar(clase):
    if clase == 'Iris-setosa\n':
        clase = 0
    elif clase == 'Iris-versicolor\n':
        clase = 1
    elif clase == 'Iris-virginica\n':
        clase = 2
for i in range(len(archivo)):
    a = archivo[i]
    a = [a[0],a[1],a[2],a[3],cambiar(a[4])]

print(archivo)