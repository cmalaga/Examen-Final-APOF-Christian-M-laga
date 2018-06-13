print("COMPARADOR DE NÚMEROS")
numero1 = int(input("Escriba un número: "))
numero2 = int(input("Escriba otro número: "))

if numero1 > numero2:
    print('El mayor es el primero: ' + str(numero1))
elif numero1 < numero2:
    print('El mayor es el segundo: ' + str(numero2))
else:
    print("Los dos números son iguales")
