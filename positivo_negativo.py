num = 0
num = int(input("Ingrese un numero que sea positivo: "))
while num < 0:
    print(num, "es un numero negativo.")
    num = int(input("Ingrese un numero positivo: "))
print("El numero ingresado es positivo.")
