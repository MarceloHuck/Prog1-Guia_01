numero = int(input("Ingrese el número a evaluar: "))
if numero < 0:
    print("Número negativo")
else:
    if numero < 10:
        print("Número positivo menor a los 2 dígitos")
    elif numero > 99:
        print("Número positivo mayor a los 2 dígitos")
    else:
        print("Número positivo de 2 dígitos")

if numero > 9 and numero < 100:
    print("Número positivo de 2 dígitos")