#Desarrolle un algoritmo que ingrese dos números y luego los imprima de forma
#ascendente.(primero se imprime el menor y luego el mayor)
# Solicitar al usuario dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1 < num2:
    print(f"Los números en orden ascendente son: {num1}, {num2}")
else:
    print(f"Los números en orden ascendente son: {num2}, {num1}")
