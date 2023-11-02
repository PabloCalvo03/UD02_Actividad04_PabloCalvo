cantidad = int(input("Introduzca la cantidad a invertir: "))
interesAnual = float(input("Introduzca el interes anual: "))
numeroAnyos = int(input("Introduce el numero de años que durara la inversion: "))

capitalObtenido = cantidad*(interesAnual/100+1)**numeroAnyos

for anyo in range(1, numeroAnyos + 1):
    capitalObtenido = cantidad * (1 + interesAnual) ** anyo
    print("Año: {}, Capital obtenido: ${}".format(anyo, capitalObtenido))