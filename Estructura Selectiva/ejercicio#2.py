#Resolver la siguiente ecuación, teniendo en cuenta que solo se puede realizar si la
#variable r es diferente de 2; en caso contrario hacer P=1 P=(r-2)3
r = float(input("Introduce el valor de r: "))
if r != 2:
    P = r - 2
    print(f"El valor de P es: {P}")
else:
    P = 1
    print("Como r es igual a 2, el valor de P es asignado a 1.")

