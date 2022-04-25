numero_accidentes = float(input("Introducir número de accidentes con una responsabilidad del 20% y mas alta: "))
distancia = float(input("Introducir distancia total viajada en el año(km): "))
años = float(input("Introducir numero de años trabajando: "))

prima= 0.01*distancia

if años >=4:
    prima=prima+200+(20*(años-4))



if numero_accidentes == 1:
    prima=prima/2

if numero_accidentes == 2:
    prima=prima/3

if numero_accidentes == 3:
    prima=prima/4

if numero_accidentes > 3:
    prima=0

print("La prima de final de año de este conductor es equivalente a: "+str(prima))