print("----------MENU DEL SISTEMA----------")
print("1. SUMAR")
print("2. RESTAR")
print("3. MULTIPLICAR")
print("4. SALIR")

op = int(input("SELECCIONE UNA DE LAS OPCIONES: "))

if op == 1:
    valorSuma1 = float(input("Ingrese primer valor a sumar: "))
    valorSuma2 = float(input("Ingrese segundo valor a sumar: "))
    suma = valorSuma1 + valorSuma2
    print("La suma de", valorSuma1, "y", valorSuma2, "es igual a", suma)

elif op == 2:
    a = float(input("Ingrese primer valor a restar: "))
    b = float(input("Ingrese segundo valor a restar: "))
    resta = a - b
    print("La resta de", a, "y", b, "es igual a", resta)

elif op == 3:
    a = float(input("Ingrese primer valor a multiplicar: "))
    b = float(input("Ingrese segundo valor a multiplicar: "))
    multiplicacion = a * b
    print("La multiplicacion de", a, "y", b, "es igual a", multiplicacion)

elif op == 4:
    print("Gracias!")

else:
    print("La opción no existe.")
