#El sistema de liquidación que hacen los conductores de buses y los colectivos a las
#diferentes empresas consiste en tomar un número de la registradora al iniciar el día y otro
#al terminarlo . La diferencia de estos dos números determina el numero de pasajeros
#transportados en el día. Realizar un algoritmo que permita leer estos dos números y el
#valor del pasaje. Calcular e imprimir el total de pasajeros, el valor liquidado al conductor y
#el total liquidado a la empresa. Tenga en cuenta que la empresa recibe tres cuartas partes del dinero mientras el conductor recibe el resto.
numeroinicial=int(input("ingrese el numero inicial de la registradora:"))
numerofinal=int(input("ingrese el numero final de la registradora:"))
preciopasaje=float(input("digite el precio del pasaje:"))

totalpasajeros=numeroinicial-numerofinal

Valortotal=totalpasajeros*preciopasaje
valorconductor=Valortotal/4
valorempresa=Valortotal-valorconductor

print(f"total de pasajeros:{totalpasajeros}")
print(f"valor liquidado al conductor:{valorconductor}")
print(f"valor liquidado a la empresa{valorempresa}")