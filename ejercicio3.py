## 25 viajes x 125 = 3125 - 20% (625) = 2500
def gastos_viajes(a, b):
    if a >= 1 and a <= 20:
        total_gastado = a * b
    elif a >= 21 and a <= 30:
        total_gastado = a * (b * 0.8)  # 20% de descuento
    elif a >= 31 and a <= 40:
        total_gastado = a * (b * 0.7)  # 30% de descuento
    else:
        total_gastado = a * (b * 0.6)  # 40% de descuento
    return total_gastado

importe = int(input("Ingrese la tarifa base del pasaje: "))
viajes = int(input("Ingrese la cantidad de viajes realizados en el mes: "))
total_gastado = gastos_viajes(viajes, importe)
print("El total gastado en viajes este mes es: ", total_gastado)