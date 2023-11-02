numeroElegido = int(input("Introduce un numero entero positivo: "))
numerosSeparadosPorComas = ""

for i in range(1, numeroElegido, 2):
    numerosSeparadosPorComas += (str(i) + ", ")

print(numerosSeparadosPorComas)