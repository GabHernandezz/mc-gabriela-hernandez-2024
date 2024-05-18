# -*- coding: utf-8 -*-
"""TALLER_24.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1l02dq3sgP_eLrPSGgZcwP-2DhGo6PS7s
"""

def multiplicar_polinomios(a,b):
  longitud = len(a) + len(b) - 1
  resultado = [0] * longitud

  for i in range(len(a)):
    for j in range(len(b)):
      resultado[i+j] += a[i] * b[j]
  return resultado

def imprimir_polinomio(p):
  texto ='f(x)='
  grado = len(p) - 1
  for i in range(len(p)):
    if p[i]==0:
      continue
    if i>0 and p[i]>=0:
      texto += '+'
    texto +=str(round((p[i]),6))
    if grado==1:
      texto += 'x'
    elif grado >1:
      texto += 'x^' + str(grado)
    grado -=1
  print(texto)

#programa principal
x = [1, 2, 3, 4, 5]
y = [2, 1.8, -2, -4.6, 3.6]

n = len(x)
polinomio = [0]*n
for i in range(n):
  numerador = [1]
  denominador = 1
  for j in range(n):
    if j != i:
      numerador = multiplicar_polinomios(numerador, [1, -x[j]])
      denominador = denominador * (x[i]- x[j])
  lixfxi = []
  for k in range(len(numerador)):
    lixfxi.append(numerador[k]/ denominador * y[i])

  for k in range(len(lixfxi)):
    polinomio[k] += lixfxi[k]


print(imprimir_polinomio(polinomio))

