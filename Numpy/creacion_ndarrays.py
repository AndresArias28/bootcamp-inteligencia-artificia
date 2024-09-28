
import numpy as np
#lista de numeros

numeros = [1,2,3,4,5,6,7,8,9,10]

#creacuibn de y un ndarray



ndarray_numeros = np.array(numeros)

print(ndarray_numeros)

#creacion de un ndarray de 3x3 con unos
matriz_unos = np.ones((3,3))

#matriz de 2x3 con ceros
matriz_ceros = np.zeros((2,3))

#matrix personalizada
matriz_personalizada = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(matriz_personalizada)
print(matriz_unos)