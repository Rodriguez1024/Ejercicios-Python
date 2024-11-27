#Un atleta tiene la costumbre de medir el tiempo(en minutos) y la distancia (en metros)
#durante sus tres días de entrenamiento. Al final de la semana quiere saber el total de
#tiempo que duro el entrenamiento , la distancia recorrida, y el promedio del tiempo y la distancia recorrida.
def calcular_estadisticas():
    tiempo_total = 0
    distancia_total = 0

    for dia in range(1, 4):
        tiempo = float(input(f"Tiempo de entrenamiento del día {dia} (minutos): "))
        distancia = float(input(f"Distancia recorrida del día {dia} (metros): "))

        tiempo_total += tiempo
        distancia_total += distancia

    promedio_tiempo = tiempo_total / 3
    promedio_distancia = distancia_total / 3

    print(f"\nTiempo total de entrenamiento: {tiempo_total:.2f} minutos")
    print(f"Distancia total recorrida: {distancia_total:.2f} metros")
    print(f"Promedio de tiempo por día: {promedio_tiempo:.2f} minutos")
    print(f"Promedio de distancia por día: {promedio_distancia:.2f} metros")

calcular_estadisticas()
