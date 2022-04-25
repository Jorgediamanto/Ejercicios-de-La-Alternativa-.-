cantidad_alumnos = float(input("Introducir numero de alumnos: "))
dias = float(input("Introducir numero de dias: "))

coste_alumno =0
coste_global =0

if cantidad_alumnos <= 25:
    print("Coste del trayecto es de 67,30 por alumno.")
    coste_alumno=67.30
    coste_global=67.30*cantidad_alumnos


if cantidad_alumnos > 25:
    print("Coste del trayecto es de 61 por alumno.")
    coste_alumno=61
    coste_global=61*cantidad_alumnos

print("Coste de la comida es de 3,50 por dia por alumno. ")
coste_alumno=coste_alumno+(3.5*dias)
coste_global=coste_global+(3.5*dias*cantidad_alumnos)

if cantidad_alumnos < 30:
    print("Coste del alojamiento es de 4,75 por alumno por dia.")
    coste_alumno= coste_alumno+(4.75*dias)
    coste_global= coste_global+(4.75*dias*cantidad_alumnos)

if cantidad_alumnos > 30 and cantidad_alumnos <36:
    print("Coste del alojamiento es de 4,00 por alumno por dia.")
    coste_alumno= coste_alumno+(4*dias)
    coste_global= coste_global+(4*dias*cantidad_alumnos)

if cantidad_alumnos > 35:
    print("Coste del alojamiento es de 3,50 por alumno por dia.")
    coste_alumno= coste_alumno+(3.5*dias)
    coste_global= coste_global+(3.5*dias*cantidad_alumnos)


print("Coste por alumno es igual a : "+str(coste_alumno))

print("Coste global del viaje es igual a : "+str(coste_global))

