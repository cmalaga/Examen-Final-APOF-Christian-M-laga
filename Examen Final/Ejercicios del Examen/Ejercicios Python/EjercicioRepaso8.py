# Programa condicion multiple

marca = input ("Escribe la marca del coche")
modelo = input ("Escribe modelo del coche")

precio1 = 10000

if marca == "ford" or marca =="Ford" or marca == "FORD":
    if modelo == "fiesta":
        descuento = 8;
    elif modelo == "focus":
        descuento = 15;
    else:
        descuento = 0;


if marca == "opel" or marca =="Opel" or marca == "OPEL":
    descuento = 20;

precio = precio1 - (precio1 * (descuento/100))

print (' El precio final es ' + str(precio) + '€')
