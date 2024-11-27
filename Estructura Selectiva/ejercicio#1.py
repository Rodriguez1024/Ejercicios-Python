#Hacer un programa para un laboratorio de Química, que lea un símbolo químico e
#imprimir a que elemento al cual corresponde.
simbolo=input("dijite el simbolo en mayuscula")
simbolo1=simbolo.upper()
if simbolo1=="H":
    print("el elemento es hidrogeno")
elif simbolo1=="O":
    print("el elemento es oxigeno")
elif simbolo1=="N":
    print("el elemento es nitrogeno")
else:
    print("ELEMENTO NO ENCONTRADO")