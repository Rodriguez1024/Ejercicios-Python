#El valor del desempleo en Ibagué aumentó en el primer trimestre un 9.5% y en el segundo
#trimestre cayó en un 1.5%. Calcular el valor del desempleo actual.
valor_desempleo=int(input("ingrese el valor del desempleo en ibague: "))
desempleo_1=valor_desempleo*0.095
desempleo_2=valor_desempleo*0.015
desempleoTotal=(valor_desempleo+desempleo_1)-desempleo_2
print("el valor de desempleo es ", desempleoTotal)