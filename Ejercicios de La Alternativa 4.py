nota1 = float(input("Introducir resultado de la nota 1: "))
nota2 = float(input("Introducir resultado de la nota 2: "))
nota3 = float(input("Introducir resultado de la nota 3: "))
nota4 = float(input("Introducir resultado de la nota 4: "))

media_alumno = (nota1+nota2+nota3+nota4)/4

if media_alumno>15:
    print("Alumno con talento")

if media_alumno<15 and media_alumno>12:
    print("Con capacidad")

if media_alumno<12:
    print("Debe reorientarse")