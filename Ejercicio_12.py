diasnotrabajados = int(input("Ingrese días no trabajados en el año: "))
anioingreso      = int(input("Ingrese año de ingreso a la empresa:  "))
sueldobasico     = 47000
adicional        = 30
antiguedad       = 5
faltas           = 0
if diasnotrabajados <= faltas and anioingreso < 2016: #Para trabajar con fechas y la función año tengo que instalar pandas...
    sueldo = sueldobasico + (sueldobasico * (adicional / 100))
else:
    sueldo = sueldobasico
print(f"Sueldo: ${sueldo}")