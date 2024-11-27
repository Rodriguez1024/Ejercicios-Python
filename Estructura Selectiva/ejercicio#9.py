#El costo de entrada a un parque de diversiones depende de la edad de las
#personas; si la persona tiene más de 1 año y menos de 4 años entra gratis; si tiene
#entre 4 y 8 años paga US $2, si tiene entre 9 y 16 años paga US $5, si tiene entre 17
#y 35 años paga US $6 y si tiene más de 35 años paga US$10. Imprimir el valor en dólares y pesos colombianos.
def costo_entrada(edad):
    if edad < 1:
        return 0, 0 
    elif 1 <= edad < 4:
        return 0, 0 
    elif 4 <= edad <= 8:
        return 2, 2 * 4000  
    elif 9 <= edad <= 16:
        return 5, 5 * 4000  
    elif 17 <= edad <= 35:
        return 6, 6 * 4000  
    else:
        return 10, 10 * 4000  

edad = int(input("Ingresa la edad de la persona: "))
costo_usd, costo_cop = costo_entrada(edad)

print(f"Costo de entrada: ${costo_usd} USD / ${costo_cop} COP")
