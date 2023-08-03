a = float(input("Ingrese primer valor: "))
b = float(input("Ingrese segundo valor: "))
c = float(input("Ingrese tercer valor: "))

if a > b and a > c:
    print("El numero mayor es:", a)

elif b > a and b > c:
    print("El numero mayor es:", b)
    
else:
    print("El numero mayor es:", c)
