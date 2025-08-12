import numpy as np
import os
#crear una matriz 3x3  
matriz = np.random.randint(0, 100, (3, 3))
print("Matriz 3x3:\n", matriz)

matriz2 = np.random.Generator(np.random.PCG64()).integers(0, 100, (3, 3))
print("Matriz 3x3 con generador:\n", matriz2)

matriz_identidad = np.eye(3)
print("Matriz identidad 3x3:\n", matriz_identidad)

matriz_transpuesta = matriz.T
print("Matriz transpuesta:\n", matriz_transpuesta)

matriz_zeros = np.zeros((3, 3))
print("Matriz de ceros 3x3:\n", matriz_zeros)

for incrementador in range(2):
    matriz_zeros[incrementador][incrementador] = 1
print("Matriz de ceros diagonal:\n", matriz_zeros)

for fila in range(2):
    for columna in range(2):
        matriz_zeros[fila][columna] = np.random.randint(0, 100) + 1
print("Matriz de ceros modificada:\n", matriz_zeros)