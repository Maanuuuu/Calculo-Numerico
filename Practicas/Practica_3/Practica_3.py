import numpy as np 

vector=np.array([1,2,3,4])
matriz=np.array([[1,2],[3,4]])
np.arange(10)

print(np.eye(3)) #Crea una matriz identidad (diagonal principal llena de 1)
print("-----------")

print(np.ones((4,5)))#Crea una matriz llena de 1
print("-----------")
print(np.zeros((4,5,2)))#Crea una matriz llena de 0 
print("-----------")
print(np.diag([1,2,3,5],2))#Crea una matriz y asigna la diagonal que especifiquemos por encima de la diagonal principal (si el parametro es 0 la diagonal especificada sera la diagonal principal)

