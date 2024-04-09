def diasiguiente(dia, mes, año):
    # Febrero tiene 28 días por defecto, 29 en años bisiestos
    febrero = 28 if mes != 2 else 29 if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0) else 28
    
    # Meses con 30 días
    treinta_dias = {4, 6, 9, 11}
    
    # Incrementamos el día
    dia += 1
    
    # Si el día sobrepasa el máximo del mes, ajustamos
    if dia > febrero if mes == 2 else 30 if mes in treinta_dias else 31:
        dia = 1
        mes += 1
        if mes > 12:  # Si el mes sobrepasa diciembre, ajustamos el año también
            mes = 1
            año += 1
            
    return dia, mes, año

# Programa para sumar N días a una fecha
def sumar_n_dias():
    a = int(input("Por favor ingrese el día: "))
    b = int(input("Por favor ingrese el mes: "))
    c = int(input("Por favor ingrese el año: "))
    n = int(input("Por favor ingrese el número de días a sumar: "))
    
    for _ in range(n):
        a, b, c = diasiguiente(a, b, c)
    
    print("La fecha después de", n, "días será:", a, "/", b, "/", c)

# Programa para calcular la cantidad de días entre dos fechas
def calcular_diferencia_de_dias():
    a1 = int(input("Por favor ingrese el primer día: "))
    m1 = int(input("Por favor ingrese el primer mes: "))
    a2 = int(input("Por favor ingrese el segundo día: "))
    m2 = int(input("Por favor ingrese el segundo mes: "))
    
    dias_totales = 0
    
    while a1 != a2 or m1 != m2:
        a1, m1, _ = diasiguiente(a1, m1, 0)
        dias_totales += 1
        
    print("La diferencia en días entre las dos fechas es:", dias_totales)

# Ejecutar el programa correspondiente
opcion = input("Seleccione la opción deseada (1: Sumar N días, 2: Calcular diferencia de días): ")

if opcion == "1":
    sumar_n_dias()
elif opcion == "2":
    calcular_diferencia_de_dias()
else:
    print("Opción no válida.")
