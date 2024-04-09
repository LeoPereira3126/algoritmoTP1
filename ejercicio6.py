def concatenar (a,b):
    concatenacion = str(a) + str(b)
    return concatenacion

num1 = int(input("Ingresar el primer número "))
num2 = int(input("Ingresar el segundo número "))
num3 = concatenar(num1, num2)
print ("La concatenación de los números es: ", num3)