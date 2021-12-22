nombre  = input("Ingrese nombre del alumno: ")
carrera = input("Ingrese carrera elegida ('D'/'E'/'T'): ")
ciudad  = input("Ingrese ciudad de origen: ") #No aplico ninguna función para "homogeneizar" la entrada (e.g.: Todas mayúsculas/minúsculas/capitalizada) y, por supuesto, no espero acentos
cuota   = 4500
desc    = 15
if carrera == "E" and ciudad != "rio cuarto":
    cuota = cuota - (cuota * (desc / 100))
print(f"Alumno : {nombre}")
print(f"Carrera: {carrera}")
print(f"Cuota  : ${cuota}")