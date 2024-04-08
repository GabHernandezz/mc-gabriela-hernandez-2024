# -*- coding: utf-8 -*-
"""TALLER_15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E0A7K7VRaPbfUB69O1GQObVVc8BHWMni

#TALLER_15
"""

import copy

def imprimirSistema(a, b, etiqueta):
    n = len(b)
    print(etiqueta)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end = " ")
        print("|", b[i])
    print()

def gaussJordan(ao, bo):
    a = copy.deepcopy(ao)
    b = copy.copy(bo)

    n = len(b)
    imprimirSistema(a, b, "Matriz inicial")
    for i in range(n):
        if a[i][i] == 0 :
          for fila in range(i+1,n):
            if a[fila][i] != 0:
              a[fila],a[i] = a[i],a[fila]
              b[fila],b[i] = b[i],b[fila]
              break
          imprimirSistema(a, b, "Pivoteo")

        pivote = a[i][i]

        #Dividir por el pivote
        for j in range(n):
            a[i][j] /= pivote
        b[i] /= pivote
        imprimirSistema(a, b, "División")

        #Reducción
        for k in range(n):
            if i != k:
                #Se reduce
                valorAux = -a[k][i]
                for j in range(n):
                    a[k][j] += a[i][j] * valorAux
                b[k] += b[i] * valorAux
        imprimirSistema(a, b, "Reducción")

    return b

a = [[3, 3, 4], [2, 2, 0], [4, 0, 1]]
b = [23, 10, 30]
x = gaussJordan(a, b)

print("Respuesta:")
for i in range(len(x)):
    print("x" + str(i+1), "=", x[i])

#Pruebas
print("\nPruebas:")
for i in range(len(b)):
    valorAux = b[i]
    for j in range(len(b)):
        valorAux -= a[i][j] * x[j]
    print("Test", i + 1, "=", valorAux)