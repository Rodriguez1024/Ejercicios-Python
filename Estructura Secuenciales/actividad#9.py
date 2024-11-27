#El propietario de una vivienda necesita renovar parte de esta, para lo cual tiene planeado
#enchapar los muros de los baños. La persona responsable de hacer este trabajo mide el
#alto y ancho de los muros. Se pide realizar un algoritmo para calcular el área del baño y el
#numero de baldosas necesarios para cubrir el baño. Sabiendo que la caja trae 3.5 metros cuadrados.
alto=float(input("digite el alto del muro en metros"))
ancho=float(input("digite el ancho del muro en metros"))
area_baño = alto*ancho
baldosas_necesarias= area_baño/3.5
print(f"el area del baño es:{area_baño}metros cuadrados.")
print(f"el numero de baldosas necesarias es:{baldosas_necesarias:.2f}")