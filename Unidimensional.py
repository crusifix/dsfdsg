#Array

import numpy as np


arreglo = np.array([1,2,3,4,5])


print(arreglo)

#Ndim= muestra las dimensiones del arreglo

print("Tiene", arreglo.ndim,"Dimensiones")


#Len(Arreglo) = Para ver el largo del arreglo

print (f"Arreglo tiene un largo de  {len(arreglo)}")

#slice
#start:stop:step = (arreglo[1:1:1])

#start = Indicamos desde donde queremos revise el arreglo

#stop = Indicamos desde donde queremos que se detenga

#step = Indicar el paso de revisión que queramos visualizar

print (arreglo[1:3:1])

#transformar un for a lista

arreglo2 = (i for i in range [1,11] ) 

arreglo2 = np.array(arreglo2)

print (arreglo2)

print("--------------------------------")

#usando for

for i in range (len(arreglo)):
    print(arreglo[i])

#valor matemático al arreglo completo

arreglo2+=5
print(arreglo2)