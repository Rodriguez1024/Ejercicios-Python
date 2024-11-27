#Un cliente de telefonía celular realiza cuatro llamadas: dos a un primer operador, y dos al
#segundo operador. El cliente desea conocer el costo de cada llamada, El costo total de las
#llamadas a cada operador, y el total de las cuatro llamadas.
def calcular_costo():
    # Costo por minuto de cada operador
    operador1 = float(input("Costo por minuto Operador 1: "))
    operador2 = float(input("Costo por minuto Operador 2: "))

    # Duración de las llamadas
    duracion_llamada1_1 = float(input("Duración Llamada 1 (Operador 1): "))
    duracion_llamada1_2 = float(input("Duración Llamada 2 (Operador 1): "))
    duracion_llamada2_1 = float(input("Duración Llamada 1 (Operador 2): "))
    duracion_llamada2_2 = float(input("Duración Llamada 2 (Operador 2): "))

    # Calcular el costo de cada llamada
    costo_llamada1_1 =operador1 * duracion_llamada1_1
    costo_llamada1_2 =operador1 * duracion_llamada1_2
    costo_llamada2_1 =operador2 * duracion_llamada2_1
    costo_llamada2_2 =operador2 * duracion_llamada2_2

    # Calcular el costo total de las llamadas a cada operador
    costo_total_operador1 = costo_llamada1_1 + costo_llamada1_2
    costo_total_operador2 = costo_llamada2_1 + costo_llamada2_2

    # Calcular el costo total de las cuatro llamadas
    costo_total = costo_total_operador1 + costo_total_operador2

    # Mostrar los resultados
    print(f"Costo Llamada 1 (Operador 1): ${costo_llamada1_1:.2f}")
    print(f"Costo Llamada 2 (Operador 1): ${costo_llamada1_2:.2f}")
    print(f"Costo Llamada 1 (Operador 2): ${costo_llamada2_1:.2f}")
    print(f"Costo Llamada 2 (Operador 2): ${costo_llamada2_2:.2f}")
    print(f"Costo Total Operador 1: ${costo_total_operador1:.2f}")
    print(f"Costo Total Operador 2: ${costo_total_operador2:.2f}")
    print(f"Costo Total: ${costo_total:.2f}")

# Ejecutar la función
calcular_costo()

