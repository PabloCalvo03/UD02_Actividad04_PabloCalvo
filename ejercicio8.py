tamaño = int(input("Ingrese el tamaño de la figura: "))

for i in range(1, tamaño + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=' ')
    print()