def calcular_vuelto(a, b):
    vuelto = b - a
    if vuelto < 0:
        print("Error: Dinero recibido insuficiente.")
        return
    
    billete_5000 = 0
    billete_1000 = 0
    billete_500 = 0
    billete_200 = 0
    billete_100 = 0
    billete_50 = 0
    billete_10 = 0

    while vuelto >= 5000:
        billete_5000 += 1
        vuelto -= 5000

    while vuelto >= 1000:
        billete_1000 += 1
        vuelto -= 1000

    while vuelto >= 500:
        billete_500 += 1
        vuelto -= 500

    while vuelto >= 200:
        billete_200 += 1
        vuelto -= 200

    while vuelto >= 100:
        billete_100 += 1
        vuelto -= 100

    while vuelto >= 50:
        billete_50 += 1
        vuelto -= 50

    while vuelto >= 10:
        billete_10 += 1
        vuelto -= 10

    if vuelto != 0:
        print("Error: No se pueden entregar billetes adecuados para el vuelto.")
        return

    print("Vuelto:")
    if billete_5000 > 0:
        print(f"{billete_5000} billete(s) de $5000")
    if billete_1000 > 0:
        print(f"{billete_1000} billete(s) de $1000")
    if billete_500 > 0:
        print(f"{billete_500} billete(s) de $500")
    if billete_200 > 0:
        print(f"{billete_200} billete(s) de $200")
    if billete_100 > 0:
        print(f"{billete_100} billete(s) de $100")
    if billete_50 > 0:
        print(f"{billete_50} billete(s) de $50")
    if billete_10 > 0:
        print(f"{billete_10} billete(s) de $10")

# Ejemplo de uso
compra = int(input("Ingrese el total de la compra: "))
dinero = int(input("Ingrese el dinero recibido: "))

calcular_vuelto(compra, dinero)
