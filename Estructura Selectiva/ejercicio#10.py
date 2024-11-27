#Elabore un algoritmo que lea el nombre, la edad, el sexo (F: Femenino, M:
#masculino) y el estado civil(1:Casado,2:soltero,3:Separado,4: otro) de una persona
#que desea participar en las elecciones este año. Si es menor de edad imprimir
#mensaje que diga que no puede votar, de lo contrario imprimir el mensaje indicado
#  la mesa en la cual le corresponde votar.
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (F/M): ").upper()
estado_civil = int(input("Ingrese su estado civil (1:Casado, 2:Soltero, 3:Separado, 4:Otro): "))

if edad < 18:
  print("Usted no puede votar.")
else:
  if sexo == 'F':
    if estado_civil == 1:
      mesa = 1
    elif estado_civil == 2:
      mesa = 2
    elif estado_civil == 3:
      mesa = 3
    else:
      mesa = 4
  elif sexo == 'M':
    if estado_civil == 1:
      mesa = 5
    elif estado_civil == 2:
      mesa = 6
    elif estado_civil == 3:
      mesa = 7
    else:
      mesa = 8
  else:
    print("Sexo inválido.")
  print(f"Usted debe votar en la mesa {mesa}.")
