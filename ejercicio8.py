def diadelasemana(dia, mes, año):
    if mes < 3:
        mes += 10
        año -= 1
    else:
        mes -= 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26 * mes - 2) // 10) + dia + año2 + (año2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    if diasem < 0:
        diasem += 7
    return diasem
 
def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
 
mes = int(input("Ingrese el número de mes (1-12): "))
año = int(input("Ingrese el año: "))
 
primer_dia = diadelasemana(1, mes, año)
 
dias_mes = 31
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias_mes = 30
elif mes == 2:
    if es_bisiesto(año):
        dias_mes = 29
    else:
        dias_mes = 28
 
print("Nombre del mes:", end=" ")
if mes == 1:
    print("Enero", end=" ")
elif mes == 2:
    print("Febrero", end=" ")
elif mes == 3:
    print("Marzo", end=" ")
elif mes == 4:
    print("Abril", end=" ")
elif mes == 5:
    print("Mayo", end=" ")
elif mes == 6:
    print("Junio", end=" ")
elif mes == 7:
    print("Julio", end=" ")
elif mes == 8:
    print("Agosto", end=" ")
elif mes == 9:
    print("Septiembre", end=" ")
elif mes == 10:
    print("Octubre", end=" ")
elif mes == 11:
    print("Noviembre", end=" ")
else:
    print("Diciembre", end=" ")
 
print("Año:", año)
 
print("Dom Lun Mar Mie Jue Vie Sab")
 
for _ in range(primer_dia):
    print("    ", end=" ")
 
for dia in range(1, dias_mes + 1):
    print(f"{dia:3}", end=" ")
    primer_dia += 1
    if primer_dia == 7:
        primer_dia = 0
        print()