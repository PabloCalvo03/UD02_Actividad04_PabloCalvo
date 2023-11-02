numero = int(input("Introduce de que numero quieres conocer la tabla de multiplicar: "))

for i in range(1, 11):
    print(str(numero) + "*" + str(i) + "=" + str(numero * i))