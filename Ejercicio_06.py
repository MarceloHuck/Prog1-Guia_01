float1 = float(input('Ingresar el primer número: '))
float2 = float(input('Ingresar el segundo número: '))
operador = input('Ingrese la operación que desea realizar ("+": sumar o "-": restar): ')
if operador == '+':
    suma = float1 + float2
    print(f"Resultado de la suma: {suma}")
else:
    resta = float1 - float2
    print(f"Resultado de la resta: {resta}")