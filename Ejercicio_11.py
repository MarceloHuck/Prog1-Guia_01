nombre  = input("Ingrese nombre del pasajero: ")
edad    = int(input("Ingrese edad del pasajero:   "))
valorpasaje = 1700
desc    = 40
if (edad > 4 and edad < 11) or edad > 65:
    valorpasaje = valorpasaje - (valorpasaje * (desc / 100))
print(f"Pasajero : {nombre}")
print(f"Pasaje   : ${valorpasaje}")