cantidad_a= int(input("Escriba el número de elementos de A (Primer conjunto): "))
A=set()

for i in range(cantidad_a):
    elementoA = int(input("Elemento: "+str(i+1)+": "))
    A.add(elementoA)
print("A=",A)
cantidad_b= int(input("Escriba el número de elementos de B (Segundo conjunto): "))
B=set()

for i in range(cantidad_b):
    elementoB = int(input("Elemento: "+str(i+1)+": "))
    B.add(elementoB)
print("B= ",B)


while True:
    print("¿Qué operación desea hacer?")
    print("1. Unión")
    print("2. Intersección")
    print("3. Diferencia")
    print("4. Diferencia simétrica")
    operacion=input("Elija su opción: ")

    if operacion == "1":
            print("La unión de los conjuntos es: ", A.union(B))
            print("Y su cardinalidad es: ", len(A.union(B)))
    elif operacion =="2":
            inter=A.intersection(B)
            print("La intersección de los conjuntos es: ", inter)
            if inter == set():
                  print("No hay intersección. Vacío")
            print("Y su cardinalidad es: ", len(A.intersection(B)))
    elif operacion =="3":
            print("La diferencia de A-B es: ", A.difference(B))
            print("La diferencia de B-A es: ", B.difference(A))
            print("La cardinalidad de A-B es: ", len(A.difference(B)))
            print("La cardinalidad de B-A es: ", len(B.difference(A)))
    elif operacion =="4":
        print("La diferencia simétrica de los conjuntos es: ", A.symmetric_difference(B))


