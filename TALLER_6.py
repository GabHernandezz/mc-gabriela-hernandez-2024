import math

x = float(input("Valor del ángulo en radianes: "))
es = (0.5 * 10**-8) * 100
ea = 100
valor = 1
iteraciones = 1

while ea > es:
    valor_ant = valor
    n = iteraciones * 2
    factorial = math.factorial(n)
    termino = ((-1)**iteraciones) * (x**n) / factorial
    valor += termino
    ea = abs((valor - valor_ant) / valor) * 100
    iteraciones += 1

cos_x = valor
ea = abs((valor - valor_ant) / valor) * 100

print("El coseno de", x, "es aproximadamente", round(cos_x, 8))
print("El error aproximado relativo porcentual es", round(ea, 8), "%")
print("Número de iteraciones realizadas: ", iteraciones - 1)