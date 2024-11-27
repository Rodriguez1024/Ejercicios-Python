#Una persona no tiene claridad sobre el dispositivo que desea comprar para su
#portátil . La decisión la tomará de acuerdo con una bonificación que recibirá de
#parte de la empresa donde labora. Su recibe menos de $50.000 comprará una cámara web.
#Si recibe entre $50.000 y $200.000 comprará un subwoofer. 
#Si recibe más de $200.000 y hasta $500.000 se comprará un DD externo. Si recibe más de $500.000 y hasta $1.000.000 
#se compra una impresora multifuncional. Y si recibe más de un $1.000.000 se comprará un proyector.
#Realice un algoritmo para ayudarle a esta persona a comprar un dispositivo.
# Solicitar la cantidad de bonificación recibida
bonificacion = float(input("Ingrese la bonificación recibida (en pesos):"))

if bonificacion < 50000:
    dispositivo = "una cámara web"
elif 50000 <= bonificacion <= 200000:
    dispositivo = "un subwoofer"
elif 200000 < bonificacion <= 500000:
    dispositivo = "un disco duro externo"
elif 500000 < bonificacion <= 1000000:
    dispositivo = "una impresora multifuncional"
elif bonificacion > 1000000:
    dispositivo = "un proyector"
else:
    dispositivo = "ningún dispositivo, la entrada no es válida."

print(f"Con una bonificación de ${bonificacion:,.2f}, la persona se comprará {dispositivo}.")
