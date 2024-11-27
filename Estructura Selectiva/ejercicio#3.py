# Calcule el promedio de goles anotados por un jugador en cuatro encuentros, solo
#si la suma de estos es mayor a 10; de lo contrario imprimir No se pide determinar el promedio.
goles_partido1 = int(input("Ingrese los goles del primer encuentro: "))
goles_partido2 = int(input("Ingrese los goles del segundo encuentro: "))
goles_partido3 = int(input("Ingrese los goles del tercer encuentro: "))
goles_partido4 = int(input("Ingrese los goles del cuarto encuentro: "))

suma_goles = goles_partido1 + goles_partido2 + goles_partido3 + goles_partido4

if suma_goles > 10:
    promedio = suma_goles / 4
    print(f"El promedio de goles anotados es: {promedio:.2f}")
else:
    print("No se pide determinar el promedio.")
