oblongo = lambda x: any(x == i * (i + 1) for i in range(1, x))

triangular = lambda x: any(x == i * (i + 1) // 2 for i in range(1,x))


prueba = oblongo(66)
print(prueba)
prueba2 = triangular(100)
print(prueba2)