def calendario(dia,mes,año):
    if (1 <= dia <= 30) and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        return True
    elif (1 <= dia <= 31) and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        return True
    elif (1 <= dia <= 28) and (mes == 2):
        return True
    elif (1 <= dia <= 29) and (mes == 2) and ( año % 4 == 0):
        return True
    else:
        return False

d = int(input("Por favor ingresar el día ")) 
m = int(input("por favor ingresar el Mes "))
a = int(input("Por favor ingresar el año "))
resultado = calendario(d,m,a)
print("fecha",d,"/",m,"/",a,"es",resultado)