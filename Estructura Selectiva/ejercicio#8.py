#Leer los tres lados del triángulo (A,BY C), imprimir el tipo de triangulo teniendo en
#cuenta que es un triángulo equilátero(solo si sus tres lados son iguales) y es un
#triángulo escaleno(si todos los lados son diferentes). Además debe validar que sus
#lados permitan formar un triángulo; la condición es que cada lado tiene que ser menos que la suma de los otros dos.
a = float(input("Ingresa la longitud del lado A: "))
b = float(input("Ingresa la longitud del lado B: "))
c = float(input("Ingresa la longitud del lado C: "))


if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("El triángulo es equilátero.")
    elif a != b and a != c and b != c:
        print("El triángulo es escaleno.")
    else:
        print("El triángulo es isósceles.")
else:
    print("Los lados ingresados no forman un triángulo válido.")

