precio_compra = float(input("Introduzca el precio de la compra: "))

if precio_compra>100 and precio_compra<500:
    precio_compra = precio_compra * 0.95

if precio_compra>500:
    precio_compra = precio_compra * 0.92

print("Precio final con descuento aplicado: "+ str(precio_compra))