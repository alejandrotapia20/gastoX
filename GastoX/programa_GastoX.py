import re           # Importamos RE para verificar requisitos de contraseña
import csv          # Importamos csv para exportar documento en formato .csv
from datetime import datetime           # Importamos datetime para verificar fecha
import matplotlib.pyplot as plt             # pip install matplotlib (Importamos Matplotlib para graficar)

def registro():         # Función de registro de usuario y contraseña
    print("\n-----Registro de usuario-----")
    usuario_registrado = False
    while not usuario_registrado:
        nombre_usuario = input("Ingrese un nombre de usuario: ")
        contrasena = input("Ingrese una contraseña: ")

        if not re.search(r"(?=.*[A-Z])(?=.*\d).{8,}", contrasena):          # Requisito de contraseña
            print("La contraseña debe contener al menos una mayúscula, un número y ser de al menos 8 caracteres.")
            continue

        print("Registro exitoso. Ahora puede iniciar sesión.")
        usuario_registrado = True
        return nombre_usuario, contrasena


def inicio_sesion(nombre_usuario, contrasena):          # Función de inicio de sesión
    print("\n-----Inicio de sesión-----")
    intentos = 3
    while intentos > 0:         # Usuario tiene 3 intentos para ingresar credenciales
        usuario_ingresado = input("Nombre de usuario: ")
        contrasena_ingresada = input("Contraseña: ")

        if usuario_ingresado == nombre_usuario and contrasena_ingresada == contrasena:
            print(f"\n¡Bienvenido, {nombre_usuario}!")
            rastreador_gastos()
            break
        else:
            intentos -= 1
            if intentos == 1:
                print(f"Credenciales incorrectas. Te queda 1 intento.")
            else:
                print(f"Credenciales incorrectas. Te quedan {intentos} intentos.")

    if intentos == 0:
        print("Has alcanzado el límite de intentos. El programa se cerrará.")

def validar_fecha(fecha):           # Esta función verifica que la fecha ingresada es válida
    try:
        fecha_objeto = datetime.strptime(fecha, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def exportar_gastos(gastos):            # Función para exportar documento
    nombre_archivo = input("Ingrese el nombre del archivo para guardar los datos (sin la extensión .csv): ")
    nombre_archivo += ".csv"

    try:
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            campo_nombres = ['Fecha', 'Descripción', 'Monto']
            writer = csv.DictWriter(archivo_csv, fieldnames=campo_nombres)
            writer.writeheader()
            for fecha, (descripcion, monto) in gastos.items():
                writer.writerow({'Fecha': fecha, 'Descripción': descripcion, 'Monto': monto})
        print(f"Datos de gastos exportados exitosamente al archivo: {nombre_archivo}")
    except Exception as e:
        print(f"Ha ocurrido un error al exportar los datos: {e}")


def rastreador_gastos():            # Función principal del rastreados de gastos
    gastos = {}
    presupuesto = float(input("Ingrese el presupuesto para el mes: "))          # Se pide un presupuesto

    while True:
        fecha = input("Ingrese la fecha (dd/mm/yyyy) del gasto o 'salir' para terminar: ")          # Ingreso de fecha de gasto
        if fecha.lower() == 'salir':
            break

        if not validar_fecha(fecha):            # Si la fecha es inválida, tiene que ingresar de nuevo
            print("Fecha inválida. Ingrese una fecha en el formato dd/mm/yyyy.")
            continue

        descripcion = input("Ingrese una breve descripción del gasto: ")        # Ingreso de descripción del gasto (cita, comida...)
        monto = float(input("Ingrese el monto gastado: "))              # Ingreso del monto del gasto
        gastos[fecha] = (descripcion, monto)

    print("\nInforme de Gastos:")           # Tabla de gastos indicando fecha, descripcion y monto
    total_gastado = 0
    for fecha, (descripcion, monto) in gastos.items():
        print(f"{fecha}\t{descripcion}\t\t${monto:.2f}")
        total_gastado += monto

    ahorro = presupuesto - total_gastado
    print("------------------------------------")
    print(f"Presupuesto del mes: ${presupuesto:.2f}")           # Resumen del mes
    print(f"Total gastado en el mes: ${total_gastado:.2f}")         # Indica si el usuario ahorro o no ahorro durante el mes
    if ahorro > 0:
        print(f"Ahorraste: ${ahorro:.2f}")
    elif ahorro < 0:
        print(f"Te pasaste del presupuesto por: ${abs(ahorro):.2f}")
    else:
        print("Gastaste exactamente tu presupuesto.")

    opcion_exportar = input("¿Desea exportar los datos de gastos? (Sí/No): ").lower()       # Opcion para exportar documento (opcional)
    if opcion_exportar == 'si':
        exportar_gastos(gastos)

    fechas_ordenadas = sorted(gastos.keys(), key=lambda x: datetime.strptime(x, '%d/%m/%Y'))
    montos_diarios = [gastos[fecha][1] for fecha in fechas_ordenadas]
    dias = range(1, len(fechas_ordenadas) + 1)
                                                            # Demuestra gráfico del mes con las fechas y el monto que se gastó.
    plt.figure(figsize=(10, 5))
    plt.plot(dias, montos_diarios, marker='o', linestyle='-')
    plt.xticks(dias, fechas_ordenadas, rotation=45)
    plt.xlabel('Fecha')
    plt.ylabel('Monto gastado')
    plt.title('Gasto diario a lo largo del mes')
    plt.grid(True)
    plt.tight_layout()

    plt.show()



if __name__ == "__main__":
    print("¡Bienvenido al Rastreador de Gastos!")           # Mensaje de bienvenida
    
    cuenta_existente = input("¿Ya tienes una cuenta? (Sí/No): ").lower()

    if cuenta_existente == 'si':            # Ejemplo de usuario ya registrado y almacenado en una base de datos.
        nombre_usuario, contrasena = "nombre_usuario", "Contraseña123"
        inicio_sesion(nombre_usuario, contrasena)
    else:
        nombre_usuario, contrasena = registro()     # Una vez registrado, puede entrar al programa.
        inicio_sesion(nombre_usuario, contrasena)