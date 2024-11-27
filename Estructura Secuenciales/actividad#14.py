taller1=float(input ("ingrese la primera nota de taller: "))
taller2=float(input ("ingrese la la segunda nota de taller: "))
porcentajeTalleres = ((taller1+taller2)/2)*0.15
print("el resultado del taller es :",porcentajeTalleres)

evaluacion1=float(input("ingrese la primera nota de evaluacion: "))
evaluacion2=float(input("ingrese la segunda nota de evaluacion: "))
evaluacion3=float(input("ingrese la tercera nota de evaluacion: "))
porcentajeEvaluacion = ((evaluacion1+evaluacion2+evaluacion3)/3)*0.30
print("el resulatado de la evaluacion es :",porcentajeEvaluacion)

trabajo_final=float(input("ingrese la nota del trabajo final: "))
porcentajeTrabajofinal=trabajo_final*0.30
print("el resultado trabajo final es: ",porcentajeTrabajofinal)

quiz1=float(input("Ingrese la nota del Quiz 1: "))
quiz2=float(input("Ingrese la nota del Quiz 2: "))
quiz3=float(input("Ingrese la nota del Quiz 3: "))
quiz4=float(input("Ingrese la nota del Quiz 4: "))
porcentajeQuiz = ((quiz1+quiz2+quiz3+quiz4)/4)*0.25
print("la nota del quiz es: ",porcentajeQuiz)

nota_definitiva= (porcentajeTalleres+porcentajeEvaluacion+porcentajeTrabajofinal+porcentajeQuiz)
print("la nota definitiva es: ",nota_definitiva)