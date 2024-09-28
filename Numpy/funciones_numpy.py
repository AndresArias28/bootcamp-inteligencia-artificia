import numpy as np

#creacion de un ndarray con valores del 0 a 9
ndarray_numeros = np.arange(10)
print(ndarray_numeros)

# valores de 2 en 2n del 0 al 10
numeros_2 = np.arange(1,10,2)
print(numeros_2)

#crear ndarray con valores del 0 a 9 en 0.5
ndarray_numeros = np.arange(0,10,0.5)
print(ndarray_numeros)

#crear ndarray con valores del 0 a 9 espaciados de 2 en 2
ndarray_numeros = np.linspace(0,1,10)
print(ndarray_numeros)

puntos_2 = np.linspace(2,10,5)
print(puntos_2)

#matriz aleatoria de 3x3
matriz = np.random.rand(3,3)
print(matriz)

#crear ndarray de 5 elemtos con numeros aleatorioa  de 0 a 1
ndarray = np.random.rand(5)
print(ndarray)