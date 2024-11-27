#Desarrolle un algoritmo que permita leer una nota entre 0.0y 5.0. Imprimir su nota
#cualitativa equivalente. Teniendo en cuenta la siguiente tabla.
# Leer la nota numérica ingresada por el usuario
nota = float(input("Ingrese una nota entre 0.0 y 5.0: "))

if 0.0 <= nota <= 5.0:
    if 4.6 <= nota <= 5.0:
        cualitativa = "Excelente"
    elif 3.6 <= nota < 4.6:
        cualitativa = "Buena"
    elif 3.0 <= nota < 3.6:
        cualitativa = "Aceptable"
    elif 2.0 <= nota < 3.0:
        cualitativa = "Insuficiente"
    elif 0.0 <= nota < 2.0:
        cualitativa = "Deficiente"
    
    print(f"La nota cualitativa equivalente es: {cualitativa}")
else:
    print("Error: La nota ingresada está fuera del rango permitido (0.0 a 5.0).")
