tabla = int(input("Ingresar la tabla que desea realizar: "))
hasta = int(input("Ingresar hasta que numero desea multiplicar: "))

for i in range(1,hasta+1,1):
    c = tabla * i
    print(tabla, "x", i, "=", c)
