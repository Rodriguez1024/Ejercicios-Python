#A un empleado le aplican una retención del 18% sobre su salario básico, y le entregan una
#Bonificación de 1.3% sobre el salario. Desarrolle un algoritmo que permita calcular e
#imprimir el salario neto y los valores de sus respectivos porcentajes.
salario=int(input("dijite el salario")) 
retencion=salario*0.18
#salarioretencion=salario-retencion
bonificacion=salario*0.013
#salariobonificacion=salario+bonificacion 
salarioneto=(salario-retencion)+bonificacion
print("el salario neto es: ",salarioneto)
print("el valor de la retencion es: ", retencion)
print("el valor de la bonificacion es: ",bonificacion)
