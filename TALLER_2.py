cantidad_u= int(input("Escriba el número de elementos de U (Conjunto universal): "))
U=set()

for i in range(cantidad_u):
    elementoU = int(input("Elemento: "+str(i+1)+": "))
    U.add(elementoU)
print("U=",U)
cantidad_as= int(input("Escriba el número de elementos de A (Segundo conjunto): "))
A=set()

for i in range(cantidad_as):
    elementoA = int(input("Elemento: "+str(i+1)+": "))
    A.add(elementoA)
print("A= ",A)


if A.issubset(U):
    print("(U ∪ A)∩ A: ")
    lau=U.union(A)
    ua=set(lau)
    na=ua.intersection(A)
    if na== set():
        print("Vacío")
    else:
        print(na)
    print("(U ∩ A)∆ A: ")
    lai=U.intersection(A)
    una=set(lai)
    dif_a=una.symmetric_difference(A)
    if dif_a == set():
        print("Vacío")
    else:
        print(dif_a)
    print("(U-A)∆ A: ")
    lad=U.difference(A)
    uma=set(lad)
    difa=uma.symmetric_difference(A)
    if difa == set():
        print("Vacío")
    else:
        print(difa)
else:
    print("A no es subconjunto de U.")
