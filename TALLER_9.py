# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VWuVuxKgL8PELbgLsNU_cJYhhQv1Y8GO

#TALLER_9
"""

import math

x = float(input("Valor del ángulo en radianes: "))
es = (0.5 * 10**-8) * 100
ea = 100
valor = 0
iteraciones = 1

while ea > es:
    valor_ant = valor
    n = 2 * iteraciones - 1
    termino = ((-1)**(iteraciones - 1)) * (x**n) / math.factorial(n)
    valor += termino
    ea = abs((valor - valor_ant) / valor) * 100
    iteraciones += 1

sen_x = valor
ea = abs((valor - valor_ant) / valor) * 100

print("El seno de", x, "es aproximadamente", round(sen_x, 8))
print("El error aproximado relativo porcentual es", round(ea, 8), "%")
print("Número de iteraciones realizadas:", iteraciones - 1)