comprador = input("Cual es el nombre de la emnpresa que desea comprar: ")
cantidad = float(input("Cuantos microprocesadores desea comprar: "))

if cantidad>10000 and cantidad<20000:
    descuento = 10
    if comprador == "COMMAQ":
        descuento = descuento-2
    if comprador == "BEL":
        descuento = descuento+1

if cantidad>20000 and cantidad<40000:
    descuento = 15
    if comprador == "COMMAQ":
        descuento = descuento-2
    if comprador == "BEL":
        descuento = descuento+1

if cantidad>40000:
    descuento = 20
    if comprador == "COMMAQ":
        descuento = descuento-2
    if comprador == "BEL":
        descuento = descuento+1

print("El descuento final es de "+str(descuento)+ "%")
