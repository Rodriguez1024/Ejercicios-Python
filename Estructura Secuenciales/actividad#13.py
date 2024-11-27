#El terreno comprado por un influencers tuvo la siguiente destinación: 40% para cultivos,
#25% Para construir vivienda, 15% para zonas verdes. Leer el área total del terreno en
#metros cuadrados e imprimir el área para cada destino, y el área que queda disponible para otros proyectos.
area_total = float(input("Ingrese el área total del terreno en metros cuadrados: "))
area_cultivos = area_total * 0.40
area_vivienda = area_total * 0.25
area_verdes = area_total * 0.15
area_restante = area_total - area_cultivos - area_vivienda - area_verdes


print("Distribución del terreno:")
print(f"Cultivos: {area_cultivos:.2f} m²")
print(f"Vivienda: {area_vivienda:.2f} m²")
print(f"Zonas verdes: {area_verdes:.2f} m²")
print(f"Área restante: {area_restante:.2f} m²")
