marca = input ("Escribe la marca de la tarjeta gráfica")
modelo = input ("Escribe modelo de la tarjeta gráfica")

if marca == "MSI" or marca =="Msi" or marca == "msi":
    descuento = 5 ;

if modelo == "GTX" or modelo =="Gtx" or modelo == "gtx":
    descuento = 10;

if modelo =="IT" or modelo =="It" or modelo == "it":
    descuento = 20

print (' El descuento es: ' )
print (descuento)
print ('%')
