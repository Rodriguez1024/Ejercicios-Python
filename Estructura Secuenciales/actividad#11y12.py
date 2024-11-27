#Una madre y sus 4 hijos se acercan a recibir información por parte de un abogado
#referente al dinero que les corresponde en una herencia dejada por su esposo y padre respectivamente.
# Entrada de datos
total_herencia = float(input("Ingrese el valor total de la herencia: "))

herencia_esposa = total_herencia * 0.40
herencia_hijo1 = total_herencia * 0.30
herencia_hijo2 = total_herencia * 0.20
herencia_hijo3 = total_herencia * 0.40
herencia_hijo4 = total_herencia * 0.10

print("Reparto de la herencia:")
print(f"Esposa: {herencia_esposa:.2f}")
print(f"Hijo 1: {herencia_hijo1:.2f}")
print(f"Hijo 2: {herencia_hijo2:.2f}")
print(f"Hijo 3: {herencia_hijo3:.2f}")
print(f"Hijo 4: {herencia_hijo4:.2f}")
