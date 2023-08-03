nota_primer = float(input("Ingrese nota primer parcial: "))
nota_segundo = float(input("Ingrese nota de segundo parcial: "))

promedio = (nota_primer + nota_segundo) / 2

if promedio >= 70:
    print("Nota final:", promedio, "Clase aprobada")
else:
    print("Nota final:", promedio, "Clase reaprobada")
