def rastreador_gastos():
    gastos_mensuales = {}  # Usaremos un diccionario para almacenar los gastos con sus descripciones

    while True:
        fecha = input("Ingrese la fecha (dd/mm/yyyy) del gasto o 'salir' para terminar: ")

        if fecha.lower() == 'salir':
            break

        descripcion = input("Ingrese una breve descripción del gasto: ")
        monto = float(input("Ingrese el monto gastado: "))

        # Almacenamos el gasto en el diccionario usando la fecha como clave y una lista como valor para almacenar la descripción y el monto.
        gastos_mensuales[fecha] = [descripcion, monto]

    # Mostramos el informe de gastos al final del mes o cuando el usuario termina de ingresar los datos.
    print("\nInforme de Gastos:")
    print("Fecha\t\tDescripción\t\tMonto")
    print("------------------------------------")
    total_gastado = 0
    for fecha, gasto_info in gastos_mensuales.items():
        descripcion, monto = gasto_info
        print(f"{fecha}\t{descripcion}\t\t${monto:.2f}")
        total_gastado += monto
    print("------------------------------------")
    print(f"Total gastado en el mes: ${total_gastado:.2f}")


if __name__ == "__main__":
    print("¡Bienvenido al Rastreador de Gastos!")
    rastreador_gastos()
