# -*- coding: utf-8 -*-
"""TALLER_17.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YFewwxUlws1gvIpZcogB8yWwVEMcGBQj

#TALLER 17

##Gráfica y valores de la tabla
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def producto(lista):
    return [x * x for x in lista]

def cuadrado(lista):
    return [x ** 2 for x in lista]

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [9, 7, 8, 5, 6, 4.5, 4, 2.5]


#Código con uso de numpy y plt

slope, intercept, _, _, _ = linregress(x, y)


x_regresion = np.linspace(min(x), max(x), 100)
y_regresion = slope * x_regresion + intercept


plt.scatter(x, y, label='Datos originales')
plt.plot(x_regresion, y_regresion, color='red', label='Regresión lineal')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def producto(lista):
    return [x * x for x in lista]

def cuadrado(lista):
    return [x ** 2 for x in lista]

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [9, 7, 8, 5, 6, 4.5, 4, 2.5]

n = len(x)
sum_xy = sum([xi * yi for xi, yi in zip(x, y)])
sum_x = sum(x)
sum_y = sum(y)
sum_x_squared = sum([xi ** 2 for xi in x])

# Calcular a1 y a0
a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
a0 = (sum_y - a1 * sum_x) / n

# Imprimir a0 y a1
print("y=",str(a0)+str(a1),"x")

# Calcular la regresión lineal
slope, intercept, _, _, _ = linregress(x, y)

# Crear la línea de regresión
x_regresion = np.linspace(min(x), max(x), 100)
y_regresion = slope * x_regresion + intercept

# Graficar los puntos y la línea de regresión
plt.scatter(x, y, label='Datos originales')
plt.plot(x_regresion, y_regresion, color='red', label='Regresión lineal')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()