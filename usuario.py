user = input("Ingrese su usuario: ")
passw = int(input("Ingrese su clave: "))

while user != "Alejandro" or passw != 12345:
    print("Usuario o clave incorrecta. Ingrese nuevamente.")
    input("Ingrese su usuario: ")
    int(input("Ingrese su clave: "))
print("Bienvenido al sistema.")


