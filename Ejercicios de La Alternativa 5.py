niños_familia = float(input("Introduzca el numero de niños en la familia: ")) 
precio_total_sindescuento = float(input("Introduzca el pago que deberia hacer toda la familia sin aplicar el descuento: "))

if niños_familia ==2:
    precio_descontado = precio_total_sindescuento * 0.1
    print("La cantidad que se descuentan es de: "+ str(precio_descontado))

if niños_familia ==3:
    precio_descontado = precio_total_sindescuento * 0.15
    print("La cantidad que se descuentan es de: "+ str(precio_descontado))

if niños_familia ==4:
    precio_descontado = precio_total_sindescuento * 0.18
    print("La cantidad que se descuentan es de: "+ str(precio_descontado))

if niños_familia > 4:
    descuento = (18 + (float(niños_familia)-4))/100
    precio_descontado = precio_total_sindescuento * descuento
    print("La cantidad que se descuentan es de: "+ str(precio_descontado))