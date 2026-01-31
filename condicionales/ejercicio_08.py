# Proceso ComprobarNotaEdadSexo
nota = int(input("Introduce la nota:"))
edad = int(input("Introduce la edad:"))
sexo = input("Introduce el sexo (F/M):")

if nota >= 5 and edad >= 18:
    if sexo.upper() == "F":
        print("Aceptada")
    elif sexo.upper() == "M":
        print("Posible")
    else:
        print("No Aceptada")
else:
    print("No Aceptada")