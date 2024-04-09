def mayor (a,b,c):
    if a > b:
        if a > c:
            if a >= 0:
                return a

    if b > c:
        if b > a:
            if b >= 0:
                return b
    
    if c > a:
        if c > b:
            if c >= 0:
                return c
    else:
        return -1

num1= int(input("por favor ingresar el primer número "))
num2 = int(input("por favor ingresar el segundo número "))
num3 = int(input("por favor ingresar el tercer número "))
maximo = mayor(num1,num2,num3)
if maximo != -1:
    print("el número maximo es", maximo)
else:
    print("no existe un número maximo")