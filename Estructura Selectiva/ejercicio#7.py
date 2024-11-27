#En las pruebas de ICFES, se presentan dos tipos de prueba: Una de aptitud
#matemática y otra de lenguaje. Leer los puntajes obtenidos por un estudiante en
#cada prueba e imprimir en cual obtuvo mayor puntaje. Tenga en cuenta que ambos puntajes podrían ser iguales.
# Leer los puntajes obtenidos en las pruebas
puntaje_matematica = float(input("Ingrese el puntaje obtenido en la prueba de aptitud matemática: "))
puntaje_lenguaje = float(input("Ingrese el puntaje obtenido en la prueba de lenguaje: "))

if puntaje_matematica > puntaje_lenguaje:
    print("El estudiante obtuvo mayor puntaje en la prueba de aptitud matemática.")
elif puntaje_lenguaje > puntaje_matematica:
    print("El estudiante obtuvo mayor puntaje en la prueba de lenguaje.")
else:
    print("El estudiante obtuvo puntajes iguales en ambas pruebas.")
