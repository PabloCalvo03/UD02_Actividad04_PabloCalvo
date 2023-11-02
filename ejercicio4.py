numeroElegido = int(input("Introduce un numero entero positivo: "))
numerosSeparadosPorComas = ""

for i in reversed(range(0, numeroElegido+1)):
    numerosSeparadosPorComas += (str(i) + ", ")

print(numerosSeparadosPorComas)
