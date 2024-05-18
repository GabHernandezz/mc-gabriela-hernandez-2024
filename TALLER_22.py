# -*- coding: utf-8 -*-
"""TALLER_22.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Hg0iKb153RVzHLQ_JppSuOJ56vjmDIxz
"""

import numpy as np

x1 = np.array([1, 1, 2, 3, 1, 2, 3, 3])
x2 = np.array([0, 1, 1, 2, 2, 3, 3, 1])
y = np.array([0.6, 2, 0.1, 0.3, 2.2, 2.3, 0.8, -1])

n = len(x1)

suma_x1 = np.sum(x1)
suma_x2 = np.sum(x2)
suma_x1_x2 = np.sum(x1 * x2)
suma_x1_cuadrado = np.sum(x1 ** 2)
suma_x2_cuadrado = np.sum(x2 ** 2)
suma_y = np.sum(y)
suma_x1_y = np.sum(x1 * y)
suma_x2_y = np.sum(x2 * y)

# Resolución del sistema de ecuaciones lineales
A = np.array([[n, suma_x1, suma_x2],
              [suma_x1, suma_x1_cuadrado, suma_x1_x2],
              [suma_x2, suma_x1_x2, suma_x2_cuadrado]])
b = np.array([suma_y, suma_x1_y, suma_x2_y])
coeficientes = np.linalg.solve(A, b)


a0 = coeficientes[0]
a1 = coeficientes[1]
a2 = coeficientes[2]

ecuacion = a0 + a1 * x1 + a2 * x2
r = (np.corrcoef(y, ecuacion)[0, 1])*100

# Suma total y residual de cuadrados, o sea St y Sr
St = np.sum((y - np.mean(y)) ** 2)
Sr = np.sum((y - ecuacion) ** 2)

print("a0:", a0)
print("a1:", a1)
print("a2:", a2)
print("r:", r)
print("St:", St)
print("Sr:", Sr)
print("Ecucación:", f"z = {a0} + ({a1}x) + {a2}y")